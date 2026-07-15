# Bold — Product Vision & Prototype

Interactive prototype and product vision page for Bold's adaptive daily guidance platform for adults 65+.

## How to Review

Open the deployed site (or serve the folder locally with `python3 -m http.server`):

- **`index.html`** — Simple index; lists every prototype, study, and spec
- **`prototype.html`** — Interactive prototype (Today, Discover, Care, Profile, Notifications)
- **`vision.html`** — Product vision & strategy

## Editing the index

The index list is driven by **`projects.json`** — `index.html` renders it at load,
so add / edit / reorder entries there rather than editing the HTML. Each entry:

```json
{
  "path": "prototype.html",
  "href": "prototype.html",
  "name": "Interactive Prototype",
  "desc": "One-line description",
  "icon": "📱",
  "author": "Izabela",
  "category": "Prototypes"
}
```

| Field | Value |
|---|---|
| `path` | Repo-relative file path (shown as the muted path label) |
| `href` | Link to open — a local file, or a full URL (e.g. a GitHub blob for Markdown) |
| `name` | Title shown on the index |
| `desc` | Subtitle (one line) |
| `icon` | Any emoji |
| `author` | `Izabela`, `Tzu-Yi`, or `Monica` |
| `category` | `Prototypes`, `Design System`, `User Research`, or `Strategy` |

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
