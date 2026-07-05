# assetgen — image asset generation via Replicate

A small, reusable toolkit for producing game/UI image assets from a declarative
JSON manifest. Standalone (not tied to Django); depends only on `requests` and
`Pillow`, both already project dependencies.

## Token

The Replicate API token is read from, in order:

1. `--token <token>` flag
2. `REPLICATE_API_TOKEN` environment variable
3. a `REPLICATE_API_TOKEN=...` line in the repo-root `.env` (git-ignored — safest)

Nothing that reveals the token is ever printed.

```bash
# one-time: drop your key into the git-ignored .env
echo 'REPLICATE_API_TOKEN=r8_your_key_here' >> .env
```

## Run

```bash
# preview resolved prompts/paths without calling the API (no token needed)
python scripts/assetgen/generate.py scripts/assetgen/manifests/officer-portraits.json --dry-run

# generate everything in a manifest
python scripts/assetgen/generate.py scripts/assetgen/manifests/officer-portraits.json

# regenerate just one or two assets
python scripts/assetgen/generate.py scripts/assetgen/manifests/officer-portraits.json --only officer-grim,officer-alert
```

Generated files overwrite the SVG placeholders' PNG slots; `officer.js` already
prefers `officer-<mood>.png` over the bundled SVG, so the new art appears with no
code change.

## Manifest format

```jsonc
{
  "defaults": {
    "model": "google/nano-banana-pro",        // any Replicate "owner/name" image model
    "image_input_key": "image_input",          // input key this model uses for reference images
    "seed": 70707,                             // optional; shared seed for models that support it
    "input": { "aspect_ratio": "1:1", "output_format": "png" },
    "resize": [512, 512],                      // optional Pillow resize after download
    "background_removal_model": null,          // optional 2nd pass, e.g. "851-labs/background-remover"
    "prompt_prefix": "...",                    // prepended to every asset prompt
    "prompt_suffix": "..."                     // appended to every asset prompt
  },
  "assets": [
    {
      "name": "officer-neutral",
      "out": "apps/webui/static/home/images/officer/officer-neutral.png",
      "prompt": "calm neutral expression",
      "input": { }                             // optional per-asset input override (merged)
    },
    {
      "name": "officer-grim",
      "out": "apps/webui/static/home/images/officer/officer-grim.png",
      "ref": ["officer-neutral"],              // reference image(s) for character consistency
      "prompt": "same officer, change only the expression to grim"
    }
  ]
}
```

Final prompt = `prompt_prefix` + asset `prompt` + `prompt_suffix`. Output paths
resolve relative to the repo root.

### Reference images (`ref`) — character/style consistency

Models like **Nano Banana Pro** accept reference images. List one or more `ref`
entries on an asset and they're passed under `image_input_key` (default
`image_input`). Each `ref` may be:

- an **asset name** generated earlier in the same run (uses its fresh output URL),
- an **asset name** generated in a previous run (reads the saved PNG as a base64
  data URI), or
- a literal **URL**, **data URI**, or **repo-relative file path**.

The officer manifest uses this: `officer-neutral` is generated first, then the
other three reference it so it's the *same* officer with only the expression
changed. Re-roll one with `--only officer-grim` and it still references the
on-disk `officer-neutral.png`.

## Adding a new asset set

Drop a new manifest under `manifests/` (e.g. `unit-icons.json`,
`map-textures.json`) and run it. For assets that need transparency (sprites,
icons), set `background_removal_model` so a second pass strips the background;
for assets composited onto a known dark UI panel, prompt a matching solid
background instead (what the officer set does with `#0B1020`).
```
