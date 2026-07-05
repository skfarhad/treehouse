---
name: site-content
description: Edit the personal website's content (bio, services, recent works, about-page experience/education/publications). Use whenever the user wants to change wording, add or remove a project or service, update job history, or fix copy on the Treehouse personal site. Knows the static-content model (no database) and where each piece of text lives.
---

# Editing the Treehouse site content

This site (Sk. Farhad's personal website) uses a **static content model** — there
is no database for site content (Option A). Content lives in two places:

## 1. Structured content — the content module

The short bio, **services**, and **recent works** live in the site content file
(`apps/website/content.py`, or the JSON/Markdown source if that's what exists).
Edit that file to change them — never reintroduce Django models or a DB for this.

Each **service** / **work** entry has these fields (mirror the existing shape):
- `title`, `description`, `body_text`
- `side_para_top` / `side_para_middle` / (`side_para_bottom` for services)
- `image_url` or `image_path`, optional `video_url`
- `category` (works only), `serial` (sort order), `show` (visibility toggle)

To hide an entry without deleting it, set `show = False`. To reorder, change
`serial`.

## 2. Prose content — the templates

The **About page** (experience, technical skills, education, publications) is
hardcoded in `apps/website/templates/website/about.html`. The footer contact
info is in `base.html`. Edit these templates directly for prose changes.

## Rules

- **Be honest and specific.** This is a professional credibility site. Don't
  invent projects, metrics, or capabilities. Ask the user for real details.
- **First-person, factual tone.** Match the voice of existing entries — concrete
  outcomes ("reduced server cost by 60%"), not marketing fluff.
- **Never publish personal home address or personal phone.** Business contact
  only. If asked to add them, flag the privacy concern first.
- **Match template idioms** — `{% load static %}`, `{% static '...' %}`, existing
  class names. Don't introduce a new CSS framework mid-page.
- After any change, run the dev server (`/runserver`) and confirm the affected
  page renders.

## Related

- Product vision & non-goals: `.claude/product/vision.md`
- What's changing and why: `.claude/product/roadmap.md`
- Project overview: `CLAUDE.md`
