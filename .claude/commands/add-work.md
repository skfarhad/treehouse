---
description: Add a new "Recent Work" / project entry to the site content
argument-hint: [project title]
---

Add a new recent-work / project entry: **$1**

The site content is static (Option A) — edit the content file, NOT the database.

1. Open the site content module (`apps/website/content.py` or the JSON/Markdown
   content source — whichever exists post-migration).
2. Add a new work entry with the same fields the existing ones use (title,
   description, body text, image, category, serial order, `show`).
3. Ask the user for any missing details (description, image path, links) rather
   than inventing them.
4. If it needs an image, confirm the file exists under
   `apps/website/static/website/assets/images/` or ask for it.
5. Run `/runserver` and confirm the new entry renders on the home page and its
   detail page.

Keep the entry's tone consistent with the existing works — factual, first-person,
concrete outcomes.
