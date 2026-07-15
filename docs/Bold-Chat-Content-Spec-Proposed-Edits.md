# Chat Service: Content Characterization — Proposed Edits

Paste-ready redlines for the existing spec. Grouped by section; each item says **what to change** and gives **final copy** where relevant.

---

## Meta / status (top of doc)
- **Status:** change from "Idea/Proposal" → the real state (e.g. "In spec / Pre-launch").
- **Target launch (July 7, 2026):** that date has passed — set a real date or mark TBD.
- **Fill the blank links:** PRD, Tech spec, **Threat model / Safety review**, Analytics, Runbook, Release plan, and **Legal/Compliance reviewer.** The empty Threat-model link is the highest-priority gap.
- Remove the blanket "all items below are TBD placeholders" caveat from sections that are now actually specified — it undersells finished work. Keep "TBD" only on genuinely open items.

---

## NEW subsection under "Safety & Guardrails" — Scope boundary

> **Scope boundary — clinical safety is defined elsewhere.**
> This spec governs **content style and UX**: greeting, character identity, latency states, message length, formatting, and emoji. It does **not** define clinical safety behavior.
> Emergency handling (directing to 911), self-harm response, the GLP-1 hold-dose protocol, and human-escalation triggers are owned by the **Agent System Prompt** and the **Threat Model / Safety Review**, which are the source of truth. This doc must not restate or contradict them.
> Required cross-links before launch: `[Agent System Prompt]` · `[Threat Model / Safety Review]`. Owner: Security/Privacy reviewer.

---

## 1) Chat greeting — revisions

**Fix the recommended greeting (it currently breaks two of our own rules: ~215 chars vs. 200 limit, and a 25-word sentence vs. the <20-word rule).**

**A (recommended) — revised, compliant (~180 chars, every sentence <20 words):**
> "Hi, I'm June, Bold's AI health assistant. I can help with nutrition and healthy-living questions. Whenever you need a person, I'll connect you with your care team. What's on your mind?"

Keep B and C as A/B variants, but trim C to fit the 200-char / above-the-fold limit.

**NEW — Returning-member greeting.** Full AI disclosure every session reads robotic. Disclosure is carried by the always-visible "AI assistant" label; the message can be short:
> "Welcome back, {{first_name}}. What can I help you with today?"
> *Policy:* show the full disclosure greeting on first session and re-disclose at a set cadence (e.g. first session each month) or per Legal guidance; the persistent "AI assistant" label is always visible.

**NEW — Contextual openers (assistant invoked from a specific place, not a cold open).** June is launched from the greeting, the header, and inline app entry points, so the first line should match the context and skip "What's on your mind?" Examples:
- From a side-effect check: *"You mentioned some nausea. I can help you think it through — and if it needs a person, I'll get your care team. What are you feeling?"*
- From a care-plan item: *"Happy to help with today's movement. What's your question?"*
- From labs: *"Looks like you're getting your labs done. Want help finding a location or how to prep?"*
- From an onboarding measurement: *"Let's get your waist measurement right. Want the quick how-to?"*
> *Policy:* AI disclosure must have occurred at least once in the session/onboarding before a contextual opener is used without it; the "AI assistant" label remains visible throughout.

---

## 2) Character name & identity — reconcile with the lexicon
- **Drop "Bold Guide."** The Bold vocabulary bans **"Guide" as a title.** Keep "Ask Bold" as the branded-tool option; human-name option stands (Remy, Ellis, **June**, Frankie, Ray).
- The Open Issue "Finalize character name" is checked ✅ but no name is recorded — **record the decision.** Working recommendation: **June** (human-name/companion direction).
- Add: **"Colorful/Playful" is achieved through vivid language, not emoji** — so the emoji ban (§7) doesn't read as fighting the brand voice.

---

## 3–5) Latency / unavailable — small fixes
- The body says "confirm thresholds against infra P50/P95," but the Open Issue for latency is marked ✅. **State the resolved numbers** (0s / 5s / 12s / 30s) as confirmed, or reopen the question — don't leave it half-closed.
- Consider whether a **30s timeout is too long for a 65+ audience** given observed 10–15s delays; validate that the ceiling isn't higher than members will tolerate (a 20–25s ceiling may test better). Keep the calm copy as written — it's good.

---

## 6) Message length — specify hard-cap behavior
- Add what happens at the **2,000-char hard cap:** block further input with a friendly, non-blaming message (never truncate silently or scold). Draft counter/warning copy:
  - Soft (≈800): *"That's a lot to work with — you can keep going, or send now and I'll help with what's here."*
  - Hard (2,000): *"This is longer than I can take in at once. Try sending the most important part first."*

---

## 8–9) Readability & long-message — consistency
- **Align reading level across docs:** this spec says 6th–8th grade; the Agent System Prompt says 8th. Pick one (recommend **"6th–8th grade"**) and state it identically in both.
- Long-message template: **cap the list at 3–5 short bullets**, each under ~20 words, to prevent the "structured wall of text."

---

## Suggested metrics — add safety/guardrail measures
Current metrics are engagement + format only. Add, for a health chat:
- **Hand-off rate** and **time-to-human** (a healthy escalation path is a feature, not a failure).
- **Guardrail compliance:** % of responses containing disallowed phrasing (diagnostic / prescriptive / futility) — **target ~0**, measured via QA/red-team sampling.
- **Re-ask rate** (member rephrases the same question) as a confusion signal, alongside the "confusing" rate.
- **Safety-event handling accuracy** from red-team scenarios (emergency, self-harm, severe side effect routed correctly).

---

## Roadmap nudge
- **Spanish / localization:** for a Medicare 65+ population this may deserve to move up from P1. Flag for prioritization.
