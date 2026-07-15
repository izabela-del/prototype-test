# Bold Care — Member App Information Architecture

**Scaling the "Today" page into a full multi-page experience**
Version 0.1 · Planning draft · Mobile-first, 65+

---

## 1. The core idea

Today you have one strong page. The move is to keep that page as the **hub** and let it stay simple by giving the deeper stuff its own **spokes** — dedicated tabs the member visits on purpose, not by accident. The homepage answers one question every time it opens: **"What is the one thing I should do right now?"** Everything else lives one tap away.

This matches the hub-and-spoke constraint in your spec and keeps cognitive load low for a 65+ audience. The member should never feel like they're "navigating an app." They land, they see today, they do the next thing.

**Design principles carried through every page**

- **One primary action per screen.** The rest is secondary.
- **The clinician is the motivator.** Surface provider directives and human contact prominently — supervision is the product's emotional core, not a safety footnote.
- **Progress over numbers.** Lead with strength, function, and "what changed," not the scale.
- **Low-friction input.** Every logging action should be doable in one tap or one photo. Never a blank form when a tap will do.
- **Bold lexicon.** Movement (not workout), Action Plan (not program), Step (not class), Members (not users), Provider, Team Bold. No emojis in the MVP.
- **Big targets, high contrast, plain language.** 8th-grade reading level, sentences under 20 words, generous tap targets.

**Visual language (from the existing Home design).** The new pages inherit the current system so nothing feels bolted on: **serif headings** (warm, trustworthy) over a clean **sans-serif body**; **purple** as the primary action color; **teal** for confirmation/success states and **green checks** for completed items; **blue→purple gradient icon chips**; white cards with soft shadows and generous rounded corners; a light-gray canvas. Desktop uses a two-column layout (primary column + a "For you today" rail); mobile stacks to a single column. The current Home page is effectively the **Pre-Appointment "To do" variant** described in §4.1 — it already has the greeting, the teal "Appointment Confirmed" card, the "To do (1/4 done)" checklist, an FAQ, and the "For you today" content rail. We're extending that same skeleton into the other phases and adding the Care / My Health / Messages spokes.

---

## 2. Navigation — recommended structure

I pressure-tested your Today / Care / My Health / Messages idea. It's the right instinct. My one adjustment: **keep it to a 4-tab bottom bar and pull the AI assistant *out* of being "just Messages"** so it can live everywhere. Here's the recommendation.

**Bottom tab bar (always visible, 4 tabs):**

| Tab | Name | Icon idea | What it is |
|-----|------|-----------|------------|
| 1 | **Today** | sun / home | The hub. Landing page + login target. Phase-aware checklist and next action. |
| 2 | **Care** | heart / people | The human layer. Care team, appointments, care plan, notes, labs. |
| 3 | **My Health** | chart / pulse | The data layer. Progress, insights, and what the member has submitted. |
| 4 | **Messages** | chat bubble | Talk to a human (Care Coordinator) *or* the Bold AI assistant, in one place. |

**Plus a persistent AI presence** that is *not* a tab. Rather than a floating chatbot bubble, June's primary entry point on Today is the **"Good morning, Carol" greeting itself** — the warmest, most human moment on the page becomes the doorway (see §6). Elsewhere she's reachable via a small, anchored "Ask June" in the header and inline contextual prompts. Think of Messages as the *home* for conversations, and the greeting + header + inline prompts as *contextual doorways* into that same assistant.

**Why 4 and not 5.** Older adults do better with fewer, fatter targets. Five tabs crowds the bar and forces tiny icons. Care Plan is important enough that people expect a tab — but it's really *content the provider writes*, so it belongs inside **Care**, not on its own. Fitness & Education aren't a tab either; the *specific lesson due today* is surfaced on **Today**, and the full library lives inside **Care Plan** (under Care). This keeps the bar calm.

**Naming note.** "Today" is the internal/spec name and works well as the landing tab even if the product name for the app is "Home." I'd keep the tab label **"Today"** — it sets the expectation that the page changes daily and is about *now*, which is exactly the behavior you want.

---

## 3. Sitemap (hub and spokes)

```
                          ┌─────────────────────┐
                          │   LOGIN / LANDING   │
                          │  (opens to Today)   │
                          └──────────┬──────────┘
                                     │
        ┌───────────────┬────────────┼───────────────┬────────────────┐
        │               │            │               │                │
   ┌────▼────┐    ┌──────▼─────┐ ┌────▼─────┐   ┌──────▼──────┐  ┌──────▼──────┐
   │  TODAY  │    │    CARE    │ │ MY HEALTH│   │  MESSAGES   │  │    JUNE     │
   │  (hub)  │    │            │ │          │   │             │  │ (everywhere)│
   └────┬────┘    └──────┬─────┘ └────┬─────┘   └──────┬──────┘  └──────┬──────┘
        │                │            │                │                │
  GREETING = June   Care Team     Progress over    Care Team chat   Greeting entry
  5-state plan     Appointments  time             AI assistant     (Today)
  Today's Movement Care Plan     Submitted data   Thread history   Header "Ask June"
  Today's Step     · Nutrition   Insights         Escalation to    Inline prompts
  Safety banner    · Movement    Lab results       human           Route into
  Next appt card   · Sleep etc.  Assessments      Notifications    Messages/AI
  Next action      Notes                          Quick replies    with context
                   Labs & orders
                   PCP info
```

Every spoke has a clear "back to Today." No page is more than 2 taps deep from the hub.

---

## 4. Page-by-page module breakdown

### 4.1 Today — the checklist, across 5 clinical states

**This is the core model.** Today is not a static homepage and not a set of parallel "user types." It is **one living plan that evolves through the clinical care pathway**, moving through five sequential states as the member hits each milestone. This comes directly from your clinical-states board.

**There is no separate "Today's Plan" concept — there's just the checklist**, and its contents change as the member moves through the states. The checklist quietly does the work the "plan" idea was meant to: it's admin tasks on day one, and care-plan actions after the visit. (We dropped the standalone "Your plan just changed" banner — it added a block without adding much; the checklist simply *being different* after a milestone is the signal.)

**The checklist mixes two item types — this distinction matters.**
- **To-do tasks (verifiable):** things the system actually knows are complete — provide measurements, complete intake, upload labs, complete lab work, watch the welcome. These have a real action ("Find a location ›", "Start ›"), check off for real, and can carry an honest progress count.
- **Honor-system habits (not verifiable):** behavioral reminders the system can't confirm — eat 140g of protein, drink 6 cups of water, move 10 minutes. These are gentle, *optional* self-report ("Mark done"), never graded, never shamed. (See the honor-system section below.)
The affordance and the copy must make the two feel different — a task you *do*, a habit you're *reminded* of.

**One checklist component, a data source that changes.** This is the highest-leverage reuse in the design: the **Day 1 setup checklist and the ongoing daily plan are the same UI** — only what fills it changes. On Day 1 it's populated by onboarding/admin tasks (intake, measurements, PCP). After the visit it's populated from **the doctor's care plan** — each prescribed directive decomposed into a concrete, checkable to-do with a cadence: "Drink 6 glasses of water" (daily), "Move 10 minutes — 3× this week" (weekly, shows 1 of 3), "Walk 6,000 steps" (daily), "Protein at 2 meals" (daily). The member always sees the same familiar "here's my list for today," and it quietly transforms from *getting set up* into *executing your care plan.* Weekly items show progress (e.g. "2 of 3 this week"); an item like "Move 10 minutes" also links into today's fitness session, so the checklist item and the content are one tap apart.

> **Product decision this raises:** the doctor writes care-plan directives as prose ("walk most days," "stay hydrated"). To render them as structured, checkable, cadenced to-dos, someone has to turn prose → structured tasks. Two options: (a) the provider selects/sets structured directives with a cadence in their tooling, or (b) the system/AI parses the prose plan into tasks for the provider to approve. Option (b) is lower provider effort but needs a clinician-approval step. This needs deciding before build — and it ties directly to the WIP clinical-pathway dependency in §8.

**It's an honor system, not a scorecard.** These reminders are *nudges pulled from the care plan*, not tasks that pass or fail. Marking something done is **optional and for the member's own satisfaction** — there are no red "incomplete" states, no "1 of 4 done" grade that reads as "3 behind," and self-report is never treated as clinical ground truth. This matters for a 65+ audience and Bold's "No Shoulds" brand: a checkbox that shames you for a missed glass of water is exactly the wrong feeling. Framing is "here's what your plan focuses on today," with a gentle "Mark done" if they want it.

**One component, three logging tiers as the product grows** — so nothing needs rebuilding:
1. **Honor reminder (MVP):** see the item, optionally tap "Mark done."
2. **Quick tally (next):** tap a counter — "3 of 6 glasses," grams of protein, minutes moved. This is the "it's 3pm, how many have you had?" idea.
3. **Auto from devices (later):** movement, steps, and weight sync from a watch or smart scale; the item shows "Synced from your watch," no manual entry.

**June is the thread that connects the tiers — and the low-friction logging interface.** Two roles: (a) **per-item helper** — each reminder has an "Ask June" for contextual help ("What does 140g of protein look like?", "Tips to drink more," "This move hurts my knee — an alternative?"); and (b) **natural-language logging** — instead of building tally UI on day one, the member simply tells June "I've had three glasses so far" and she updates the count. This bridges the honor-system MVP straight to granular logging without new UI. A "How am I doing?" entry lets June reflect progress supportively ("Water and movement are in — protein's the one for this evening. Want an easy idea?"), and a gentle, opt-in afternoon check-in is possible later, kept calm and never nagging.

Two supporting principles from the board:

- **Checklist format kills decision fatigue.** One clear set of actions per day — a paperwork task, *or* today's movement + education — never ten open choices. "Just tell me what to do today."
- **The plan is the operational hub for their care, not a fitness app.** Early on its first job is literally clinical admin (finish paperwork, schedule labs, confirm medication received). Utility and safety credibility come before "content."

**Shared skeleton across states:** June greeting (front door, §6 — and for medication states, the **daily med check-in folds into this greeting block**, not a separate card) → conditional safety banner → **the checklist** (the one clear set of items) → connection (appointment / next milestone). Priority order never changes: **safety → the checklist → connection.**

**Keep Today calm — default to "Focused."** Early drafts stacked too much on one screen (greeting + suggested prompts + evolution banner + side-effect check + plan + directive + refill + an education rail = ~7 competing blocks). For a 65+ audience that reads as overwhelming. The rule going forward: **Today shows the greeting, the one thing to do now, and at most one contextual item; everything else moves to the tab it belongs to.** Specifically off Today — the education/"For you" rail (→ a Learn/Explore surface or below the fold), progress stats (→ My Health), and the full care-plan directive list (→ Care). The wireframe has a **Focused / Full toggle** (default Focused) that demonstrates this: Focused hides the secondary modules and the suggested-prompt chips, and shows small "moved to My Health / Care" hints so nothing feels lost. "Full" is only there to show what's being held back.

> **State 1 — Sign-up → Paperwork.** *Trigger:* sign-up confirmation — "Your checklist is ready — complete your intake forms to get started." The plan's **first job is clinical admin, not content.** Modules: a setup checklist (intake form, baseline measurements, movement/sit-to-stand check with a how-to video, add PCP, upload past labs) with progress, and a locked "we'll book your first visit once paperwork's in." Automated daily SMS reminders (a launch dependency).

> **State 2 — Paperwork done → Visit (pre-visit).** *Trigger:* booking confirmation — "Your full personalized plan unlocks after your appointment." Gives them something useful while they wait: **foundational** movement + education that's safe for everyone. *Key tension to handle:* "How does a generic plan know what's right for me before I've talked to a doctor?" So be **honest that it's foundational, not yet personalized**, and set the expectation that the real plan unlocks after the visit. The confirmed appointment card is the pinned payoff.

> **State 3 — Post-visit → Labs.** *Trigger:* after the visit, the plan surfaces **"Complete your labs"** as the action item; lab completion later becomes its own trigger ("Your results are in; your provider will review and update your plan"). *Key tension:* "Is what I'm seeing actually based on what my doctor said, or is it still generic?" So the update must be **visibly different and explicitly attributed** — a "Updated after your visit with Dr. Desai" banner, and the daily plan is now personalized to the care plan. Labs are the prominent next step; results route to the provider.

> **State 4 — Labs back → On medication.** *Trigger:* "Your plan has been updated for your first week on medication — here's what to focus on." **Medication start is a high-anxiety moment**, so exercise and education are calibrated *down* to the titration phase (a trust signal: "I have less energy since starting — is this too much?"). Modules: the **daily side-effect check** (see below), an eased-in movement + "what to expect" education, and refill-review readiness ("in 6 days; meds aren't auto-renewed").

> **State 5 — Maintenance / Follow-up.** *Trigger:* follow-up scheduled — "Your plan will update after your next appointment." Now the **daily habit itself is the trigger** — the member opens because the checklist is part of their routine (plus reminders). Modules: steady daily movement + education, a **momentum** module foregrounding function ("sit-to-stand 10 → 14"), a compact ongoing side-effect check for those on medication, and next-follow-up prep. The plan keeps evolving with each visit.

**Where does the daily side-effect check live?** States 4 and 5 (anyone on medication). It is **safety-critical but calm**: not a vague mood face, and *not* a scary symptom list shown every day. It uses **progressive disclosure with an affirming default** — a gentle prompt ("How's the medication treating you? Most days, this is all it takes"), a prominent one-tap **"I'm doing well today,"** and a quiet secondary **"I've noticed something ›"** that reveals the specific symptoms only when tapped. Mild symptoms open June with tailored guidance; the severe "can't keep food or water down" path triggers the **hold-dose protocol + one-tap handoff to the care team**.
  - *Why hide the list by default:* surfacing symptoms daily has a **nocebo effect** — it primes people to notice/report symptoms they wouldn't otherwise, and a daily "can't keep food or water down" prompt raises health anxiety in a 65+ audience, against Bold's agency-affirming, no-scare-tactics brand. Safety isn't lost: anyone who feels unwell is motivated to tap "I've noticed something," and the severe path is still two taps away.
  - *Titration note:* in the first 2–4 weeks, have June proactively educate on what to watch for — via onboarding and chat, **not** a daily scary tile.

**Medication vs. lifestyle-only — how it fits the 5 states.** The five states are the spine for everyone. Medication eligibility is a *variation within* States 3–5, not a separate track: a lifestyle-only member still moves Sign-up → Paperwork → Visit → (plan personalized) → Maintenance, but **State 4 has no "on medication" framing** — instead it's "your personalized plan is active," and there's no daily side-effect check. For those members, lead harder on the **momentum module** (function and metabolic change) so value feels real without the medication narrative.

> **Tracking-problem solutions (applies across variants):** never show a blank form. Use (1) **one-tap loggers** — tap a specific symptom or "I'm fine" for the daily safety check, tap a number stepper for steps; (2) **photo-first meal logging** — snap the plate, AI drafts the entry, member confirms (MVP can stub this as "snap + we'll follow up," full AI in phase 2); (3) **conversational logging via Ask June** — "I walked to the mailbox and back today" becomes a logged activity; (4) **measurement how-to cards** — a 20-sec video shows how to measure waist correctly, then one field. Reframe logging as *checking in with your care team*, not data entry.

### 4.2 Care — the human + clinical layer

The spoke that makes supervision tangible. Sections:

- **Your Care Team.** Photos, names, roles (Provider, Trainer, Care Coordinator). Tap a person → their role, and a "Message" button. This makes the accountability partner *visible*.
- **Appointments.** Upcoming (join/reschedule/add-to-calendar) and past. Clear callout for **mandatory refill reviews** with the "not auto-renewed" reminder. Booking flow lives here.
- **Care Plan.** The provider-written, AI-drafted directives, grouped by pillar (Nutrition, Movement, Sleep, etc.), each as a bold action ("Walk 6,000 steps on most days"). This is also the door to the **full Movement & education library** (today's items are surfaced on Today; everything else is browsable here).
- **Notes / Visit summaries.** After-visit summaries in plain language. "What we discussed, what's next." (MVP: read-only provider notes shared with the member.)
- **Labs & orders.** Requisitions, "go get your blood drawn" status, results when back, upload past labs. (See §5 for the Today-vs-Care decision.)
- **PCP info.** The member's primary care provider on file, editable.

### 4.3 My Health — the data + insight layer

Where "what I submitted" and "what it means" live. Deliberately separate from Care so clinical actions stay uncluttered.

- **Progress overview.** Lead with **strength & function** (sit-to-stand trend, waist-to-height), then body composition framing (lean vs. fat), then weight/BMI last. "Lose fat, not strength" made visible.
- **Trends & insights.** Simple, explained charts. Each insight says *why it matters in plain words* ("Your sit-to-stand is improving — that's real strength you're keeping."). No jargon, no confidence scores.
- **Your submissions.** A calm log of what the member has entered — measurements, assessments, side-effect logs, meals — viewable and editable. Builds trust ("I can see my own data").
- **Assessments.** History of functional assessments and the ability to retake when prompted.

> **MVP vs vision for charts:** MVP can show 2–3 hero trends (sit-to-stand, waist-to-height, weight) as simple line/number cards. Rich body-composition visualizations and AI-written insight narratives are phase 2.

### 4.4 Messages — human + AI in one inbox

One place for all conversation, two modes:

- **Care Team thread.** Message a Care Coordinator; report side effects; ask logistics. Clear expected-response-time. This is the human escalation path.
- **Ask June (AI assistant).** The AI health assistant, following your Bold AI Chat Agent spec (expert-friend tone, explainable, cites reputable sources, never diagnoses, escalates to humans, no emojis, <600 char answers, plain language).
- **Seamless handoff.** The AI can *route to a human* at any time ("Let me get your care team on this") — a first-class button, not a dead end. Conversely a human can share an AI answer.
- **Notifications / quick replies.** Appointment reminders, lab-ready alerts, and provider messages land here too, so Messages doubles as the member's inbox.

---

## 5. Two structural decisions (from your framing questions)

**Q: AI/camera — manual from day one, or prominent AI button?**
Recommendation: **design the UI to feature a prominent "Ask June" and photo-capture affordance from day one, even if the MVP backend is partly manual.** Put the button there now so the mental model forms early and you don't re-teach navigation later. Behind it, MVP can do "snap a photo, a coordinator/AI follows up"; phase 2 turns on real photo-based meal parsing. The *placement* is permanent; the *intelligence* grows.

**Q: Assessments — visualize immediately, or clinician-only data collection?**
Recommendation: **collect in MVP, visualize the hero metrics (sit-to-stand, waist-to-height) in My Health as soon as there are 2+ data points.** Seniors care about *function over the scale* — showing "10 → 14 reps" is the single most motivating thing you can surface, and it costs little. Deeper clinical metrics can stay clinician-facing at first.

**Q: E-labs — Today module or a Tasks/To-Do spoke?**
Recommendation: **both, by state.** When there's an *action due* (go get blood drawn, results need review), it surfaces as a **Next Action / safety item on Today** because it's time-sensitive. The *full lab history and ordering* lives in **Care › Labs**. Today shows the urgent slice; Care holds the archive. This mirrors how appointments work.

---

## 6. AI contextual entry points (the journey layer)

**Naming decision.** The assistant is given a **human first name — "June"** (warm, plainspoken, easy to read and say; reads as a knowledgeable friend, which your research says older adults prefer over a "tool"). "June" is a placeholder to A/B test post-launch, per your spec. Note your own lexicon bans "Guide," "Coach," and "Buddy" as titles, so the "Bold Guide" option is out. Entry-point wording is **action-framed, not a repeated brand imperative**: the floating button reads "Ask June," and inline prompts are contextual ("How do I measure?", "Why this?", "What does this mean?") rather than a generic "Ask Bold" chip everywhere.

The assistant shouldn't only be a tab you remember to visit. It should appear *where a question naturally arises*, pre-loaded with context, and always route to a human when needed. Below is the map of entry points across the journey. Each inline entry opens the same June assistant, but seeded with the relevant context so the member doesn't have to explain themselves.

**Global**

- **The Today greeting** ("Good morning, Carol") is June's primary, most-human entry point — an active greeting card with a tap-to-ask field and suggested prompts, not static text.
- **A small anchored "Ask June" in the header** on every screen (next to the profile avatar). Reachable everywhere, but anchored — not a floating bubble that covers content.
- **Messages tab** as the conversational home.

**Onboarding / Pre-Appointment**

- On the **intake form**: "Not sure what this asks? Ask June." (explains a question in plain language)
- On the **Movement Assessment**: "How do I do the sit-to-stand safely?" → AI + video.
- On **baseline measurements**: "How do I measure my waist correctly?"
- On the **welcome/education**: "What does preserving muscle mean for me?"
- Pre-first-visit: "What should I expect at my first appointment?" (reduces no-shows via reassurance)

**Active care — daily**

- On the **daily side-effect check**: tapping a symptom like nausea opens June ("is this normal?") with tailored guidance; the severe path (can't keep food/water down / persistent vomiting) *bypasses chit-chat* and surfaces the **hold-dose protocol + one-tap human handoff** directly.
- On **today's Movement**: "This exercise hurts my knee — what can I do instead?"
- On **meal logging**: photo → "Ask June to log this" → AI drafts entry.
- On the **Care Plan directive**: "Why 6,000 steps? What if I can't hit it?" (explainability builds trust)
- On the **refill-review card**: "What happens at my refill review?"

**Insights / My Health**

- Next to each trend: "What does this mean?" → plain-language explanation of the member's *own* data ("Your strength is holding — here's why that matters").

**Care / logistics**

- On **appointments**: "Can you help me reschedule?" → AI assists, hands off to booking or coordinator.
- On **labs**: "Where's my nearest Quest? How do I prep?"

**Safety guardrails on every AI surface** (per your agent spec): never diagnose or prescribe; explain *why* using the member's own history/data; cite reputable sources with full anchor text; fail closed and honest; always offer a clear path to a human; no numeric confidence scores; no emojis; plain, warm, no-"shoulds" language.

---

## 7. MVP vs. vision — what to build first

**MVP (ship this)**

- 4-tab nav + floating Ask June button (button present even if AI is basic).
- The checklist across all 5 clinical states, mixing verifiable to-do tasks with honor-system habits; med check-in folded into the header for medication states.
- Explicit one-tap side-effect check with severe-symptom escalation + photo-capture stub + measurement how-to cards.
- Care: care team, appointments (incl. refill-review flagging), Care Plan directives, PCP info, basic labs status, read-only visit notes.
- My Health: 2–3 hero trend cards (sit-to-stand, waist-to-height, weight), "your submissions" log.
- Messages: human care-team thread + AI assistant with escalation-to-human.
- Core inline AI entry points: intake help, assessment how-to, side-effect check, care-plan "why."

**Phase 2 (fast-follow)**

- Real photo-based meal parsing (AI drafts, member confirms).
- Conversational logging via Ask June ("I walked to the mailbox").
- Richer insight narratives (AI-written, explainable) and body-composition visualizations.
- Full contextual AI entry points across every module.
- Visit-note summaries auto-generated in plain language.

---

## 8. Open questions for you

1. **App/product name for the landing tab** — keep "Today," or is there a brand name (Home) you want members to see?
2. **AI assistant name — decided: "June"** (human-name/companion direction; "Bold Guide" ruled out by your own lexicon banning "Guide" as a title). Placeholder to A/B test post-launch. If you prefer a different first name (Remy, Ellis…), it's a one-line swap everywhere.
3. **Notifications** — do reminders (appointments, labs, refills) live inside Messages, in a separate bell, or both? I've assumed Messages doubles as the inbox.
4. **Caregiver access** — any need for a spouse/adult child to view or help manage the account? Common in 65+ products; would change permissions and possibly nav.
5. **Wearables** — members dislike being *forced* onto wearables, but do we support optional connection for those who have one? Affects My Health data sources.
6. **Web + mobile parity** — is this mobile-only, or does the web dashboard need the same IA? (I've designed mobile-first, but the structure scales to web.)
7. **Nav reconciliation** — your clinical-states board shows a slightly different nav than this plan: **Messages + Settings in a top bar** and only **three bottom tabs** (Home/Today, My Health, Care), plus a **"TO DOs"** label. I've used 4 bottom tabs (Today, Care, My Health, Messages) with June + profile in the header. These are close; two things to decide: (a) does **Messages** belong in the bottom bar or the top bar, and (b) is **"TO DOs"** a separate destination or — as I've modeled it — simply *the Today checklist itself*? **Settings** should live in the profile menu regardless. Easy to switch to the 3-tab + top-bar model if you prefer it.
8. **Clinical pathway is a hard dependency (WIP).** Your board flags this in red: the milestone sequence and triggers (intake → visit → labs → prescribe → follow-up) are still being defined by clinical ops, and **the checklist's state logic depends on that work.** The five states and their transitions here are the design intent; the exact trigger events and timing need clinical ops to lock before build.
```
