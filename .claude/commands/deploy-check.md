---
description: Run pre-deploy safety and security checks before shipping
---

Run the pre-deploy checklist for the production site. Report a clear pass/fail
summary; do not deploy anything.

1. `DJANGO_SECRET_KEY=dummy-for-check poetry run python manage.py check --deploy`
   — DEBUG defaults off, so this exercises the production posture; surface
   every security warning. (The dummy key just lets the check boot.)
2. Confirm `DEBUG` defaults to `False` (only on when `DJANGO_DEBUG` is set).
3. Confirm `SECRET_KEY` is sourced from `DJANGO_SECRET_KEY`, not hardcoded, and
   that production raises if it is missing.
4. Confirm `ALLOWED_HOSTS` is restricted (not `['*']`).
5. Confirm no `*.db` files are staged for commit (`git status`).
6. Confirm no personal home address / personal phone number is present in
   `apps/website/templates/website/base.html`.
7. `poetry run python manage.py collectstatic --noinput --dry-run` to verify
   static assets resolve.

List each check with ✅ / ❌ and what to fix for any failure.
