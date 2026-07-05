# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

**Treehouse** — Sk. Farhad Uddin Ahmed's personal website. A Django app that
renders a single-person portfolio/résumé site (home, about, services, recent
works). Currently deployed via Docker on Railway.

Owner: Sk. Farhad Uddin Ahmed — Lead Software Engineer & AI Expert (IQVIA).

## Current architecture

- **Django 4.2**, single env-driven `conf/settings.py`, Python 3.9, Poetry.
- **No database.** `DATABASES = {}`. Site content lives in
  `apps/website/content.py` (short bio, services, works). There is no ORM,
  admin, auth, or sessions.
- Only two installed apps: `django.contrib.staticfiles` and `apps.website`.
  `apps.website` holds views, urls, helpers, `content.py`, templates, static —
  no `models.py`, no migrations.
- Templates: `apps/website/templates/website/` — extend `base.html`.
  Frontend is a 2013 Bootstrap 3 template ("Initio" by GetTemplate).
- Static assets: `apps/website/static/website/assets/`.
- Serving: Gunicorn + WhiteNoise for static files. `entrypoint_web.sh` runs
  collectstatic then gunicorn (no `migrate` — there's no DB).

**Do NOT reintroduce a database or ORM models for site content.** Edit
`content.py`. If a real blog is ever wanted, prefer Markdown files over a DB
(see `.claude/product/roadmap.md`). `backend.db` is kept locally, untracked,
only as a backup of the original data.

## Security posture (do not regress)

- `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` are environment-driven in
  `conf/settings.py`. DEBUG defaults OFF; prod requires `DJANGO_SECRET_KEY`
  (raises if missing). Local dev: set `DJANGO_DEBUG=1`. See `.env.example`.
- Prod (DEBUG off) enables SSL redirect + HSTS + nosniff + `X-Frame-Options`,
  with `SECURE_PROXY_SSL_HEADER` for Railway's TLS-terminating proxy.
- Do NOT hardcode secrets or default DEBUG on. Do NOT republish the personal
  home address or phone in `base.html` (privacy — business email only).

## Front-end assets

- Bootstrap 3.4.1 CSS/JS and jQuery 1.12.4 are **self-hosted** under
  `apps/website/static/website/assets/` (the dead `netdna.bootstrapcdn.com`
  CDN is gone). Glyphicons fonts are vendored so `collectstatic` (WhiteNoise
  manifest) can rewrite the CSS `url()`s. Font Awesome 6 + Google Fonts still
  load from live CDNs. Do NOT reintroduce a dead/removed CDN.

## Known issues still open

- Footer mixes Bootstrap 5 utility classes (`col-12`, `me-2`, `mb-4`) onto the
  Bootstrap 3 grid — cosmetic spacing only. Tracked in the roadmap.

## Conventions

- Content lives in one place — edit the content file, not templates, for
  bio/services/works text.
- Match the surrounding template style (Django template tags, `{% static %}`).
- Keep the project dependency-light. Question any new dependency.

## Commands

See `.claude/commands/`. Common ones: `/runserver`, `/deploy-check`,
`/add-work`, `/add-service`.
