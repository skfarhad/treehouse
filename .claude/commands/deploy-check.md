---
description: Run pre-deploy safety and security checks before shipping
---

Run the pre-deploy checklist for the production site. Report a clear pass/fail
summary; do not deploy anything.

1. `poetry run python manage.py check --deploy --settings=conf.settings_prod`
   — surface every security warning.
2. Confirm `DEBUG` is `False` in the prod settings path.
3. Confirm `SECRET_KEY` is sourced from an environment variable, not hardcoded.
4. Confirm `ALLOWED_HOSTS` is restricted (not `['*']`) for prod.
5. Confirm no `*.db` files are staged for commit (`git status`).
6. Confirm no personal home address / personal phone number is present in
   `apps/website/templates/website/base.html`.
7. `poetry run python manage.py collectstatic --noinput --dry-run` to verify
   static assets resolve.

List each check with ✅ / ❌ and what to fix for any failure.
