---
description: Add a new service entry to the site content
argument-hint: [service title]
---

Add a new service entry: **$1**

The site content is static (Option A) — edit the content file, NOT the database.

1. Open the site content module (`apps/website/content.py` or the JSON/Markdown
   content source).
2. Add a service with the fields existing services use (title, description,
   body text, side paragraphs, image, serial order, `show`).
3. Ask for any missing copy rather than inventing claims about capabilities.
4. Run `/runserver` and confirm it renders in the Services section and its
   detail page.

Keep it honest and specific — services should reflect real, deliverable
expertise (backend, AI/ML, agentic systems, automation).
