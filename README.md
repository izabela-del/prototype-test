# Bold — Product Vision & Prototype

Interactive prototype and product vision page for Bold's adaptive daily guidance platform for adults 65+.

## How to Review

Open in any browser — no build tools required:

- **`index.html`** — Product vision & strategy (homepage)
- **`prototype.html`** — Interactive prototype (Today, Discover, Care, Profile, Notifications)

## Design Principles

- **Confidence, not intensity** — we reduce uncertainty, not gamify completion
- **65+ accessible** — 44px tap targets, 4.5:1 contrast, keyboard nav, reduced motion
- **Responsive** — desktop sidebar + mobile hamburger/bottom nav
- **Warm, not clinical** — trainer-led, narrative progress, no jargon

## Repository Structure

Deployed pages live at the root so their public URLs stay stable; supporting
files are grouped into folders.

```
index.html            Landing page / directory (links to everything below)
vision.html           Product vision & strategy
prototype.html        Interactive prototype  → styles.css, app.js
styles.css, app.js    Prototype styles & behavior
_redirects            Netlify redirects

Bold-*.html           Spec & exploration pages (linked from index.html)
images/, logo/        Assets used by the deployed pages

docs/                 Written specs & content (Markdown)
scripts/              Python asset generators (icons, sky stills, avatars)
assets/               Source/working images not embedded in the deployed site
  ├─ icons/           icon-* source art
  ├─ sky/             sky-* time-of-day art
  └─ screens/         design screenshots
```
