---
description: Start the Django dev server and confirm the site renders
---

Start the local development server for the personal website.

1. Run `poetry run python manage.py runserver` (use the dev settings —
   `conf/settings.py` — not prod).
2. If the port is taken, pick the next free port.
3. Confirm the home page (`/website/home/`) and about page load without error.
4. Report the local URL and any warnings from startup.

Do NOT run `migrate` unless the user asks — under the Option A migration we are
moving away from the database.
