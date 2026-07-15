# To-Do Card — Component Spec

The **To-Do card** is the atomic unit of the **Today → "To do"** list. One card = one action the member can take today. Cards share a single layout and swap a **trailing control** + behavior per variant.

Reference implementation: `Bold-Wireframes.html` (`planItem()` / `checklist()` / `.ci-card`). Figma: Member Dashboard → node `969-13205`.

---

## 1. Where it lives & what it means

The "To do" list is **pulled from the member's care plan, authored by their provider.** It updates after each visit.

- Section header: **To do** + live count `(2/4 done)`.
- Sub-copy under the header: *"Pulled from the care plan your provider wrote for you — this list updates after each visit."*
- Footer note distinguishes the two behavioral families:
  - **To-do tasks** (labs, measurements) — the system can verify these; they check off when actually done.
  - **Daily habits** (water, protein, movement) — honor-system; the member marks what they like, or tells Bold in natural language.

**Source model**

| Source | What it is | Example |
|---|---|---|
| **Care plan** (provider-authored) | Specific directives written by the member's provider; changes after visits. | "Complete your lab work", "Eat 100g of protein" |
| **Recommended** (program-level) | Not visit-specific. Best-practice actions surfaced for everyone; can deep-link to the **Bold weight-management program** (movement plan, classes, education). | "Move 10 minutes" → *Open your Bold movement plan* |

The **fitness portion is "recommended"** content. It appears in Today like any other card, but its pills can link back to the full Bold program rather than to a provider-specific instruction.

---

## 2. Anatomy

```
┌──────────────────────────────────────────────┐
│  ( 🍗 )   Eat 100g of protein        [ ✓ Done ]│   ← head row
│           Protects your muscle                 │
│                                                │
│  [ Foods high in protein ] [ Quick recipes ]   │   ← pills row (optional)
└──────────────────────────────────────────────┘
   icon      heading + optional subcopy   trailing control
  (left)          (flex, grows)            (right, pinned)
```

- **Icon** — left, always present. 40×40 circle, blue fill, white glyph/emoji.
- **Heading** — required. One line preferred; wraps if long.
- **Subcopy** — **optional.** The "why" or provenance. Omit for compact cards (heading-only).
- **Trailing control** — right-pinned; varies by variant (see §4).
- **Pills row** — optional; full-width below the head row. AI quick-actions or program links.

---

## 3. Design tokens

| Token | Value |
|---|---|
| Card background | `#FFFFFF` |
| Card border | `1px solid #E5E5E5` |
| Card radius | `16px` |
| Card shadow | `0 12px 16px -4px rgba(16,24,40,.08), 0 4px 6px -2px rgba(16,24,40,.03)` |
| Card padding | `16px` |
| Card gap (head ↔ pills) | `13px` |
| Head row gap (icon ↔ text ↔ control) | `12px`, top-aligned |
| Icon | `40×40`, radius `50%`, bg `#4361EE`, glyph `18px` white, shadow `0 3px 8px rgba(67,97,238,.28)` |
| Heading | `16px / 600`, `#171717`, line-height `1.3` |
| Subcopy | `14px / 400`, `#4D4D4D`, line-height `1.4`, margin-top `3px` |
| Pill | bg `#F4EFFF` (hover `#EBE1FF`), radius `16px`, padding `8px 14px`, `14px / 600` `#171717` |

**Trailing controls**

| Control | Spec |
|---|---|
| Done button (`.ci-done`) | bg `#fff`, border `1px #D4D4D4`, radius `8px`, padding `5px 9px`, `14px/600 #171717`; circle `15px` w/ `1.6px #A3A3A3` ring. |
| Done — checked (`.on`) | Border + text + filled circle = green. |
| CTA button (`.ci-cta`) | border `1px` purple, bg purple-soft, purple text, radius `8px`, padding `5px 11px`, `14px/600`. Label ends with ` ›`. |
| Synced badge (`.synced`) | purple text on purple-soft, `11.5px/700`, radius `20px`. Read-only. |
| Tally stepper (`.tally`) | `– [n of target] +`; step buttons `26px` circle; count in purple. |

---

## 4. Variants

All variants share the layout above. They differ by **trailing control** and **tap behavior**. Driven by item props (`kind` / `type`).

### 4.1 To-do task (verifiable) — `kind:'task'`
- **Control:** purple CTA (`Find a location ›`, `Start ›`). When complete → static green `✓ Done`.
- **Behavior:** CTA opens a flow/AI context. System can verify completion.
- **Use for:** labs, measurements, intake form, add PCP.
- **Subcopy:** what + provenance — *"Dr. Desai ordered baseline labs · results go straight to them"*.

### 4.2 Honor habit — `type:'honor'` (default)
- **Control:** toggle `✓ Done` (tap on/off).
- **Behavior:** honor-system; no verification. Also completable via natural language to Bold.
- **Use for:** protein, water, movement reminders.
- **Subcopy:** the "why" — *"Protects your muscle"*, *"Protects your kidneys"*.

### 4.3 Device-synced — `type:'device'`
- **Control:** read-only synced badge (`⌚ 12 min today`). No manual toggle.
- **Behavior:** auto-completes from connected device.
- **Use for:** movement pulled from a watch.

### 4.4 Tally / counter — `type:'tally'`
- **Control:** stepper (`– 3 of 6 +`).
- **Behavior:** increment through the day; completes at target.
- **Use for:** cups of water.

### 4.5 Medication — `kind:'med'`
- **Control:** `✓ Done` button.
- **Behavior:** on tap → marks done **and opens a side-effect check** (Nausea / Dizziness / Can't keep food or water down / Something else, plus "✓ No side effects today"). "Can't keep food or water down" escalates to the safety flow.
- **Use for:** taking the weekly dose.
- **Subcopy:** *"Your weekly dose · check in for side effects after"*.

### 4.6 Recommended fitness (links to Bold program)
- Any of the above (usually honor), but **pills deep-link to the Bold weight-management program** rather than a provider directive.
- **Pills:** *Ask about this move* · *Open your Bold movement plan*.
- Signals that the item is program-recommended, not visit-specific.

---

## 5. Content variants (orthogonal to §4)

Each behavioral variant can also toggle:

| Dimension | Options |
|---|---|
| **Subcopy** | Present (why/provenance) · **Omitted** (compact, heading-only) |
| **Pills** | None · 1–2 AI quick-actions · Program link |
| **State** | Default · In-progress (tally) · Done (green check, dimmed) |

**Compact rule:** drop subcopy when it only restates the heading (e.g. "Eat protein" + "across your meals"). Keep it when it carries the *why* or provenance.

---

## 6. Item schema (props)

```js
{
  i: '🍗',                 // icon glyph (required)
  t: 'Eat 100g of protein',// heading (required)
  src: 'Protects your muscle', // subcopy (optional)
  type: 'honor',           // 'honor' | 'device' | 'tally'   (behavioral family)
  kind: 'task',            // 'task' | 'med'                 (overrides type control)
  done: false,             // completed state
  // task:
  cta: 'Find a location',  // CTA label (task)
  ai:  'Where is my...',   // AI context opened by CTA / single pill
  aiLabel: 'Ask Bold',     // label for the single AI pill
  // tally:
  n: 3, target: 6,
  // device:
  n: '12 min today',
  // pills (AI actions or program links):
  pills: [{ c: 'Foods high in protein', a: '<Bold reply>' }, ...]
}
```

**Control resolution order:** `type:'device'` → synced badge · `type:'tally'` → stepper · `kind:'task'` → CTA/static done · `kind:'med'` → done + side-effect flow · else → honor toggle.

---

## 7. Copy guidelines

- **Heading:** verb-first, specific, one line. *"Eat 100g of protein"*, not *"Protein intake"*.
- **Subcopy:** the *why* or where it came from — never repeat the heading. ≤ ~6 words where possible.
- **CTA label:** action + ` ›` (*Find a location ›*).
- **Numbers come from the care plan.** Protein target = 1.4–1.6 g/kg of the member's target weight (e.g. 140 lb → ~100 g/day). Keep card numbers consistent with the Care → Nutrition directive.
- **Consistent glyphs:** protein 🍗, water 💧, strength/movement 💪/🧘, medication 💊, labs 🩸.
