#!/usr/bin/env python
"""Generate image assets from a declarative JSON manifest via Replicate.

Standalone (not Django). Run from the repo root:

    python scripts/assetgen/generate.py scripts/assetgen/manifests/officer-portraits.json

The Replicate token is read from (in order): ``--token``, the ``REPLICATE_API_TOKEN``
environment variable, or a ``REPLICATE_API_TOKEN=...`` line in the repo-root ``.env``
(which is git-ignored). Nothing is printed that reveals the token.

Manifest format
---------------
{
  "defaults": {
    "model": "black-forest-labs/flux-dev",
    "input": { "aspect_ratio": "1:1", "output_format": "png", "go_fast": false },
    "seed": 7,                       // shared seed → consistent character across assets
    "prompt_prefix": "...",          // prepended to every asset prompt
    "prompt_suffix": "...",          // appended to every asset prompt
    "resize": [512, 512],            // optional Pillow resize (px) after download
    "background_removal_model": null // optional: e.g. "851-labs/background-remover"
  },
  "assets": [
    { "name": "officer-neutral",
      "out": "apps/webui/static/home/images/officer/officer-neutral.png",
      "prompt": "neutral, composed expression",
      "seed": 7,                     // optional per-asset override
      "input": { }                   // optional per-asset input override
    }
  ]
}

Per-asset ``input`` is merged over ``defaults.input``; ``seed`` overrides the
default seed. Output paths are resolved relative to the repo root.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import ReplicateClient, ReplicateError, output_urls  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_token(cli_token: str | None) -> str:
    if cli_token:
        return cli_token
    env = os.environ.get("REPLICATE_API_TOKEN")
    if env:
        return env
    dotenv = REPO_ROOT / ".env"
    if dotenv.exists():
        for line in dotenv.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("REPLICATE_API_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise ReplicateError(
        "No Replicate token. Set REPLICATE_API_TOKEN in the environment or .env, "
        "or pass --token."
    )


def build_prompt(defaults: dict, asset: dict) -> str:
    parts = [
        defaults.get("prompt_prefix", "").strip(),
        asset.get("prompt", "").strip(),
        defaults.get("prompt_suffix", "").strip(),
    ]
    return ", ".join(p for p in parts if p)


def build_input(defaults: dict, asset: dict, prompt: str) -> dict:
    model_input = dict(defaults.get("input", {}))
    model_input.update(asset.get("input", {}))
    model_input["prompt"] = prompt
    seed = asset.get("seed", defaults.get("seed"))
    if seed is not None:
        model_input.setdefault("seed", seed)
    return model_input


def download(url: str) -> bytes:
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    return r.content


def file_to_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def resolve_refs(refs, generated_urls: dict, name_to_out: dict) -> list[str]:
    """Turn ref entries into image_input values Replicate can fetch.

    A ref may be: an asset name produced earlier this run (uses its fresh output
    URL), an asset name produced in a previous run (reads the saved PNG as a
    base64 data URI), or a literal URL / data URI / repo-relative file path.
    """
    resolved: list[str] = []
    for ref in refs:
        if ref in generated_urls:
            resolved.append(generated_urls[ref])
        elif ref in name_to_out:
            p = (REPO_ROOT / name_to_out[ref]).resolve()
            if not p.exists():
                raise ReplicateError(
                    f"Reference asset '{ref}' has not been generated yet ({p})."
                )
            resolved.append(file_to_data_uri(p))
        elif ref.startswith(("http://", "https://", "data:")):
            resolved.append(ref)
        else:
            p = (REPO_ROOT / ref).resolve()
            if not p.exists():
                raise ReplicateError(f"Reference '{ref}' not found.")
            resolved.append(file_to_data_uri(p))
    return resolved


def save_image(data: bytes, out_path: Path, resize) -> None:
    img = Image.open(BytesIO(data))
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")
    if resize:
        img = img.resize(tuple(resize), Image.LANCZOS)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)


def generate_asset(client: ReplicateClient, defaults: dict, asset: dict,
                   *, dry_run: bool, generated_urls: dict, name_to_out: dict) -> str | None:
    """Generate one asset; return the model's source image URL (for ref reuse)."""
    prompt = build_prompt(defaults, asset)
    out_path = (REPO_ROOT / asset["out"]).resolve()
    refs = asset.get("ref") or []
    ref_note = f"\n  ref: {', '.join(refs)}" if refs else ""
    print(f"\n[{asset['name']}]\n  -> {out_path.relative_to(REPO_ROOT)}{ref_note}\n  prompt: {prompt}")
    if dry_run:
        return None

    model_input = build_input(defaults, asset, prompt)
    if refs:
        key = defaults.get("image_input_key", "image_input")
        model_input[key] = resolve_refs(refs, generated_urls, name_to_out)

    output = client.run(defaults["model"], model_input)
    urls = output_urls(output)
    if not urls:
        raise ReplicateError(f"{asset['name']}: model returned no image URL.")
    image_url = urls[0]

    bg_model = defaults.get("background_removal_model")
    if bg_model:
        print(f"  removing background via {bg_model} ...")
        bg_out = client.run(bg_model, {"image": image_url})
        bg_urls = output_urls(bg_out)
        if bg_urls:
            image_url = bg_urls[0]

    save_image(download(image_url), out_path, defaults.get("resize"))
    print("  OK saved")
    return image_url


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifest", help="Path to the asset manifest JSON.")
    ap.add_argument("--token", help="Replicate API token (else env / .env).")
    ap.add_argument("--only", help="Comma-separated asset names to generate.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print resolved prompts/paths without calling Replicate.")
    args = ap.parse_args(argv)

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    defaults = manifest.get("defaults", {})
    assets = manifest.get("assets", [])
    if args.only:
        wanted = {n.strip() for n in args.only.split(",")}
        assets = [a for a in assets if a["name"] in wanted]
    if not assets:
        print("No assets to generate.", file=sys.stderr)
        return 1

    client = None
    if not args.dry_run:
        client = ReplicateClient(load_token(args.token))

    # name -> output path for ALL manifest assets, so refs resolve even when a
    # filtered (--only) run relies on an asset generated in a previous run.
    name_to_out = {a["name"]: a["out"] for a in manifest.get("assets", [])}
    generated_urls: dict[str, str] = {}

    failures = 0
    for asset in assets:
        try:
            url = generate_asset(client, defaults, asset, dry_run=args.dry_run,
                                 generated_urls=generated_urls, name_to_out=name_to_out)
            if url:
                generated_urls[asset["name"]] = url
        except Exception as e:  # keep going; report at the end
            failures += 1
            print(f"  FAILED {asset.get('name', '?')}: {e}", file=sys.stderr)

    print(f"\nDone. {len(assets) - failures}/{len(assets)} generated"
          + (f", {failures} failed." if failures else "."))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
