# Roadmap

Ordered by priority. Checkboxes track state.

## Now — Option A migration (de-database)

- [x] Extract short bio, `Service`, `WorkHistory` rows into a content module
      (`apps/website/content.py`). NOTE: pulled from `backend.db`, which was the
      CURRENT data — `backend_prod.db` was stale (old ACI job, localhost images).
- [x] Rewrite `HomePage` / detail views to read from `content.py`. Detail views
      now return a proper 404 on bad/missing `id` (was a 500 IndexError).
- [x] Remove Wagtail + `taggit` + `modelcluster` from `INSTALLED_APPS`,
      `pyproject.toml`, and middleware.
- [x] Delete the dead blog (`apps/blog`, blog/sidebar templates, their views
      and URLs).
- [x] DECISION: went **fully DB-less**. Removed all content models + admin,
      and dropped `admin`/`auth`/`sessions`/`messages`/`contenttypes`, the
      `apps.user` and `apps.portfolio` apps, and all migrations. `DATABASES={}`.
      Remaining apps: `staticfiles` + `apps.website`.
- [x] Dropped SQLite from the repo (`git rm --cached`; `*.db` gitignored).
      `backend.db` kept locally only as a source-of-truth backup; deleted the
      stale `backend_prod.db`.
- [x] Reconciled deploy: removed `migrate` from `entrypoint_web.sh`,
      regenerated `poetry.lock` (wagtail-free), bumped Dockerfile Poetry to 2.2.1
      to read the new lock format.

**Migration complete.** The app is a static-content Django site with no database.

## Next — security & privacy hardening

- [ ] Move `SECRET_KEY` to an environment variable.
- [ ] Set prod security headers (SSL redirect, HSTS, secure cookies).
- [ ] Remove home address + personal phone from the footer; keep business email.
- [ ] `manage.py check --deploy` should pass clean.

## Then — frontend credibility

- [ ] Replace dead `netdna.bootstrapcdn.com` assets (self-host or modern CDN).
- [ ] Fix Bootstrap 3 vs 5 class mismatch in the footer.
- [ ] Real `<title>` / meta description / Open Graph tags; fix `author` meta.
- [ ] Proofread About page typos ("Elesticsearch", "applicationscan", "s piral").

## Maybe later — only if he starts writing

- [ ] Markdown-file blog: `.md` files in `posts/`, a view parses front-matter +
      Markdown → HTML. No database. Adding a post = committing a file.

## Someday — bigger swing

- [ ] Full frontend rebuild (static Astro/Tailwind one-pager) or drop Django for
      a static host. Consider only if maintenance of the Django path becomes a
      burden. See product/vision.md non-goals.
