---
name: site-content
description: Edit the personal website's content (bio, services, recent works, about-page experience/education/publications). Use whenever the user wants to change wording, add or remove a project or service, update job history, or fix copy on the Treehouse personal site. Knows the static-content model (no database) and where each piece of text lives.
---

# Editing the Treehouse site content

This site (Sk. Farhad's personal website) uses a **static content model** — there
is no database for site content (Option A). Almost all content lives in one
place:

## 1. Structured content — the content module

The short bio, **services**, **recent works**, **job experience**,
**education** and **publications** all live in
`apps/website/content.py`. Edit that file to change them — never reintroduce
Django models or a DB for this.

- **service** / **work**: `title`, `description`, `body_text`,
  `side_para_top` / `side_para_middle` / (`side_para_bottom` for services),
  `image_url` or `image_path`, optional `video_url`, `category` (works only)
- **experience**: `company`, `company_url`, `role`, `location`, `date_start`,
  `date_end`, `description` (HTML), `media` (list of `{image, alt, caption}`)
- **education**: same shape as experience but `institution` /
  `institution_url` / `degree` instead of `company` / `role`
- **publications**: `title`, `date`, `publisher`, `description` (plain text),
  `url`

All entries share `serial` (sort order, ascending) and `show` (visibility
toggle) — set `show = False` to hide an entry without deleting it.

These render via the `timeline-*` / `publication-*` CSS classes in
`apps/website/static/website/assets/css/styles.css` (Experience and
Education pages) and the `service-card` / `project-card` classes (Services
and Projects pages) — the shared design system for this site. Reuse those
classes for new sections rather than inventing new inline styles.

## 2. Prose content — the templates

Page framing (headings like "Job Experience", intro copy) lives in the
templates themselves (`experience.html`, `education.html`, `skills.html`).
The footer contact info is in `base.html`. Edit these templates directly for
that kind of prose change.

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
