# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

**Treehouse** — Sk. Farhad Uddin Ahmed's personal website. A Django app that
renders a single-person portfolio/résumé site (home, about, services, recent
works). Currently deployed via Docker on Railway.

Owner: Sk. Farhad Uddin Ahmed — Lead Software Engineer & AI Expert (IQVIA).

## Current architecture

- **Django 4.2** (`conf/settings.py`, `conf/settings_prod.py`), Python 3.9, Poetry.
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

## Known issues to respect (do not regress)

- `SECRET_KEY` is hardcoded in `conf/settings.py` — should move to env var.
  (Lower risk now that there are no sessions/auth, but still fix it.)
- `DEBUG=True` in base settings; no prod security headers beyond defaults.
- Personal home address + phone are published in `base.html` footer — a privacy
  issue; keep business contact only.
- Dead CDN: `netdna.bootstrapcdn.com` (Bootstrap 3 / jQuery 1.10). Footer mixes
  Bootstrap 5 utility classes onto a Bootstrap 3 grid.

These are tracked in the roadmap; fix them deliberately, don't silently
reintroduce.

## Conventions

- Content lives in one place — edit the content file, not templates, for
  bio/services/works text.
- Match the surrounding template style (Django template tags, `{% static %}`).
- Keep the project dependency-light. Question any new dependency.

## Commands

See `.claude/commands/`. Common ones: `/runserver`, `/deploy-check`,
`/add-work`, `/add-service`.
