---
name: r2d2-ds-agent
description: Governance-aware design-system agent for imToken DS work. Use for Figma DS audits, canonical page work, token parity, spacing cleanup, DS-to-design generation, design-to-demo generation, prompt-to-demo generation, and DS-to-code handoff. This skill orchestrates figma-use, audit-design-system, figma-generate-library, and related DS skills, and requires users to install missing dependent skills before continuing.
---

# R2D2@DS

Top-level coordinator skill for DS governance and handoff work.

---

## North Star

The **canonical source token JSON** and the **DS Figma variable/component definitions** are the joint authority for all execution in this skill.

Every output — Figma design, prototype, demo, or code — must be traceable to DS primitives, semantic tokens, patterns, or components. If a decision cannot be traced to one of those layers, it is either a documented DS gap or an error.

DS is not a soft reference. It is the constraint the agent must navigate around, not through.

When the DS is incomplete, the agent's job is to reach the deepest DS layer that exists, report the gap, and not silently invent a replacement.

---

## Fast Route Selector

**Read this first. Do not start tools, edits, or downstream skills until routing is complete.**

Use the first rule that matches. Stop at the first match. Do not evaluate remaining rules.

```
IF the request is about DS structure, tokens, bindings, naming,
   canonization, parity, drift, or governance records
→ DS Governance

ELSE IF the input is an existing Figma design AND the user wants
        a Figma design as the final output
→ DS To Design

ELSE IF the input is an existing Figma design AND the user wants
        a demo, prototype, or non-production implementation
→ Design To Demo

ELSE IF the input is a prompt, PRD, or product intent AND the user wants
        a Figma design as the final output
→ DS To Design   (re-route from Prompt To Demo — Figma output overrides)

ELSE IF the input is a prompt, PRD, or product intent AND the user wants
        a demo, prototype, or non-production implementation
→ Prompt To Demo

ELSE IF the output requires production-facing implementation quality,
        stable code mapping, or handoff-grade code output
→ DS To Code

ELSE
→ STOP. State the two most plausible routes and ask the user to confirm.
```

### Routing Examples

| User says | Route |
|-----------|-------|
| "audit the color bindings on this page" | DS Governance |
| "generate a Send Token flow screen in Figma using the DS" | DS To Design |
| "turn this Figma design into a clickable prototype" | Design To Demo |
| "build me a demo from this prompt using our DS" | Prompt To Demo |
| "I want a Figma screen from this PRD" | DS To Design |
| "generate production-ready React code from this Figma surface" | DS To Code |
| "this Figma link — make a demo" | Prompt for clarification (design source or prototype?) |

### Triage Output

After routing, state the following before any execution:

- chosen scenario
- primary input source (DS system state / existing Figma / prompt-or-PRD)
- output surface (DS update / Figma design / demo-prototype / production code)
- task type (repair / generation / handoff)
- routing confidence in plain language (high / medium / low + reason)

---

## Confirmation Gate

After routing, the agent must confirm the scenario with the user **once** before any substantial execution.

This is a hard requirement. It cannot be waived by:

- tool or environment permissions
- whether the routing seems obvious
- whether the user supplied detailed artifacts (Figma link, PRD, token file)

### Confirmation message shape

> "This looks like `[Scenario]`. I'll work from `[input source]` and deliver `[output surface]`. Continuing unless you want a different route."

One sentence is enough. Do not explain the full routing logic unless the user asks.

### Hard triggers that always require a stop-and-confirm before proceeding

The agent must stop and explicitly confirm with the user before taking any of the following actions, even mid-run:

1. Switching the output surface (e.g., from demo to Figma write-back)
2. Writing to a Figma canonical page for the first time in this session
3. Modifying, overwriting, or deleting a node that is not in a clearly scoped workspace or draft area
4. Changing a DS token value, collection name, or variable structure
5. Creating a net-new DS component, variant axis, or token collection
6. Proposing a DS-level semantic decision not supported by the current source token JSON
7. Choosing between two plausible scenarios where the output surface is different
8. Proceeding when more than one required input is missing simultaneously
9. Performing a multi-page write without prior classification of page roles

If any hard trigger fires mid-run, pause immediately, surface the trigger to the user with a one-line explanation, and wait for confirmation before continuing.

### Gate bypass condition

If the user already explicitly confirmed the scenario for the same task in the current thread, do not ask again unless the task materially changes.

---

## Incomplete DS Execution Protocol

When the DS is missing a required layer for a region, component, or decision, the agent must follow this fallback order strictly and stop at the first layer that is available.

**Do not skip layers. Do not blend layers. Use the deepest available layer and report what was used.**

```
Tier 1 — Canonical DS component
  A defined, reusable component exists in the DS library or canonical Figma page.
  → Use it directly. Import by key. Do not rebuild it locally.

Tier 2 — Canonical DS pattern
  No full component exists, but a pattern (layout rule, spacing system,
  interaction model) is documented in the DS.
  → Follow the pattern. Do not deviate from its layout language.

Tier 3 — Semantic token
  No component or pattern exists, but a semantic token maps the intent
  (e.g., background/card, text/primary, fill/action).
  → Compose from semantic tokens only. Do not use primitives directly.

Tier 4 — Primitive token
  No semantic token maps the intent, but a primitive token exists
  (e.g., gray.900, spacing.16, blue.600).
  → Use the primitive token. Mark the result as "primitive approximation"
    in the delivery report.

Tier 5 — Explicit gap + local approximation
  No DS layer covers the need.
  → Build the smallest possible local approximation.
  → Immediately report the gap to the user with:
       - what was needed
       - which DS tier was expected to cover it
       - what approximation was used instead
       - what the user should add to the DS to fix it permanently
  → Do NOT treat the approximation as DS-backed output.
  → Do NOT silently incorporate it into a DS confidence claim.
```

### Stop condition within the protocol

If Tier 5 would require inventing a semantic rule, business pattern, or interaction model that is not supported by any DS layer and is also not inferable from the intent source, stop before building. Surface the gap to the user and ask for direction.

---

## Global Non-Negotiable Requirements

This section is the authoritative source for skill-wide hard rules.

All agents using this skill must follow these rules before applying any scenario-specific workflow. If any statement elsewhere in this skill is softer, shorter, or ambiguous, this section takes precedence.

### 1. Route first

- Semantically classify the request using the Fast Route Selector before selecting downstream skills, tools, or execution order.
- Classify from user intent and target output surface, not artifact type alone.
- If more than one scenario is still plausible after applying the decision tree, stop and ask the user instead of guessing.

### 2. Confirm before substantial execution

- After routing, confirm the chosen scenario with the user once using the Confirmation Gate.
- Do not treat tool permission, environment permission, obviousness, or detailed input artifacts as a reason to skip confirmation.
- Do not perform substantive tool use, Figma reads or writes, file edits, or downstream skill execution before confirmation, unless the user already explicitly confirmed the same scenario for the same task in the current thread.
- Respect all hard triggers listed in the Confirmation Gate section.

### 3. Require the right inputs

- Do not continue if required skills for the selected workflow are unavailable.
- Do not continue if required inputs for the selected workflow are missing.
- For all `to AI demo` scenarios, treat the canonical source token JSON as required input rather than optional context.
- For prompt-driven demo work, also require a usable intent source such as a prompt, PRD, product note, or design brief.

### 4. Respect canonical authority

- Treat the canonical source token JSON, the relevant DS Figma definitions, and the relevant DS component or pattern definitions as the authority for execution.
- Do not treat DS inputs as soft inspiration or visual reference only.
- Do not change SSOT or adapter structure without verifying the semantic impact.
- If Figma, token JSON, and the target artifact disagree, stop and determine which layer is canonical instead of blending them loosely.

### 5. Use the required execution layer

- Use `figma-use` for serious Figma reads and writes.
- Do not assume a single fixed Figma file; work across the relevant DS surfaces for the task.
- Prefer canonical component pages over governance or history pages for active component or application work.
- Do not treat historical cleanup pages as the default handoff surface.

### 6. Apply the Incomplete DS Execution Protocol

- For every major region, component, and visual decision, apply the 5-tier fallback in the order defined above.
- Do not skip tiers. Do not blend layers from different tiers without reporting the gap.
- Report every Tier 5 approximation explicitly in the delivery report.

### 7. Enforce DS truthfulness

- Do not claim DS usage based only on visual similarity or a Figma source screenshot.
- Do not report an output as DS-backed without stating the depth reached:
  - visual approximation only
  - primitive token aligned
  - semantic token aligned
  - pattern-driven
  - canonical DS component driven
- If reusable large DS components do not exist, fall back to primitive and semantic token composition before loose approximation.

### 8. Stop instead of inventing

- Stop and ask when scenario, page role, token ownership, component boundary, or output surface is unclear.
- Stop and ask when the task would require inventing DS semantics, business patterns, or handoff assumptions not supported by the provided sources.
- If missing confidence comes from the DS side, pause instead of silently creating new system rules.

### 9. Validate and report

- Audit before and after meaningful edits when the selected workflow involves DS inspection or application.
- After meaningful Figma writes, validate with both node structure and screenshots when possible rather than relying on one alone.
- If screenshot output conflicts with node data, report the mismatch explicitly instead of guessing.
- After any substantial execution, deliver a Skill-Wide Delivery Report using the fixed format defined in the Delivery Report section.

---

## Prerequisites

### Required Skills

- `figma-use`
- `audit-design-system`
- `figma-generate-library`

### Optional Skills

- `sync-figma-token`
- `apply-design-system`
- `rad-spacing`
- `clarify`
- `normalize`
- `figma-implement-design`
- `figma-code-connect-components`
- `edit-figma-design`
- `figma-generate-design`

### Mature-Family Only

- `cc-figma-tokens`
- `cc-figma-component`

Only use mature-family tools when the token contract or component family is already stable enough for regenerate-style workflows.

### Required Inputs

- The canonical source token JSON for the current DS context.
- The relevant Figma file or page involved in the current task.
- Supporting governance docs or workflow notes when available.
- For prompt-driven demo generation, also require the intent source when available, such as a prompt, PRD, product note, or other design brief.

For all `to AI demo` scenarios, the canonical source token JSON must be treated as required input rather than optional context.

This applies to:

- `Design To Demo`
- `Prompt To Demo`

### Required Schema

- A token-to-Figma adapter schema when the task involves DS synchronization, token optimization, or adapter JSON updates.
- A governance schema or rule doc when the task involves canonical pages, naming rules, or AI-to-code readiness.

For `to AI demo` work, adapter JSON is not always required. Use it only when DS semantics cannot be read directly enough from source token JSON and Figma, or when the team already relies on an adapter-defined semantic layer.

### Generic Token Shapes

#### Source token shape

```json
{
  "<foundation-layer>": {
    "<token-namespace>": {
      "<token-group>": {
        "<token-name>": {
          "$type": "<type>",
          "$value": "<value>"
        }
      }
    }
  }
}
```

#### Adapter JSON shape

```json
{
  "<collection>/<mode>": {
    "<token-path>": {
      "$type": "<type>",
      "$value": "<value>"
    }
  }
}
```

---

## Child Skill Invocation Gates

This section defines exactly when each child skill must be invoked, when it must not, and when it is optional. Replace all "when needed" usages with these gates.

### `figma-use`

**Must invoke when:**
- Reading or writing any Figma node, page, frame, component, variable, or style
- Validating DS variable bindings, component structure, or layout hierarchy in Figma
- Any step requires structural metadata from the Figma file

**Must not invoke when:**
- The task is source token JSON analysis only (no Figma read or write needed)
- The task is documentation or governance record update only

**Optional:**
- For quick structural confirmation after a generation step if `get_metadata` is sufficient without script execution

---

### `audit-design-system`

**Must invoke when:**
- The scenario is `DS Governance` and drift analysis is the primary task
- The scenario is `DS To Design` before applying DS changes
- The scenario is `Design To Demo` before demo generation from a Figma source
- Any task requires confirming whether a Figma surface is canonical before acting on it

**Must not invoke when:**
- The task is intent-driven from a prompt alone with no Figma source to audit
- The task is a pure token JSON comparison with no Figma surface involved

**Optional:**
- Post-generation validation in `Prompt To Demo` if the output surface is Figma

---

### `figma-generate-design`

**Must invoke when:**
- The scenario is `Prompt To Demo` and the output is a Figma screen or page built from intent
- The scenario is `DS To Design` and a full-page or multi-section layout must be generated from scratch using DS components

**Must not invoke when:**
- The task is editing an existing screen (use `figma-use` for targeted edits instead)
- The task is purely governance or token audit work

**Optional:**
- `Design To Demo` if the source Figma design is missing an entire section that must be generated before demo work can proceed

---

### `apply-design-system`

**Must invoke when:**
- A Figma surface needs section-level or page-level DS reconnection before any generation or handoff step
- The scenario is `DS To Design` and the surface has significant binding drift identified by `audit-design-system`

**Must not invoke when:**
- The task is only a bounded single-node edit (use `figma-use` instead)
- The DS layer is not stable enough yet to apply — apply requires a stable token and component foundation

**Optional:**
- `Design To Demo` when bounded drift repair is needed before demo generation

---

### `rad-spacing`

**Must invoke when:**
- The spacing system has significant drift and is identified as the primary issue in an audit

**Must not invoke when:**
- Spacing is not the primary issue
- The task is generation rather than repair

**Optional:**
- Any scenario where layout hierarchy needs cleanup after application

---

### `figma-implement-design`

**Must invoke when:**
- The scenario is `DS To Code` and node-to-code fidelity is the primary deliverable
- The user explicitly requires production-facing code output from a stable Figma surface

**Must not invoke when:**
- The Figma surface is not yet stable or canonical
- The scenario is demo-oriented (`Design To Demo` or `Prompt To Demo`)

---

### `figma-code-connect-components`

**Must invoke when:**
- The scenario is `DS To Code` and the component family is stable enough for durable code mapping
- The user explicitly asks for Code Connect mapping as a deliverable

**Must not invoke when:**
- The component family naming or variant axes are unstable
- The scenario is not `DS To Code`

---

### `clarify` / `normalize`

**Must invoke when:**
- Copy, labels, or state names are ambiguous and blocking the current step
- Conventions need unification after a broad DS application pass

**Must not invoke when:**
- The primary issue is structural or token-binding, not naming or copy

---

## DS Governance

Use this scenario when the goal is to keep the DS complete, readable, stable, and governable.

### Governance Requirement

Require the canonical SSOT token source before proceeding with meaningful governance work. If missing, stop and tell the user it must be provided. Governance decisions need a formal semantic record, not only current Figma state.

### Execution Order

1. Identify the target surface.
2. Inspect the current state with `figma-use`.
3. Audit drift, bindings, naming, and structure with `audit-design-system`.
4. Decide whether the change belongs in Figma, SSOT, adapter JSON, or docs.
5. Apply the smallest correct change with `figma-use`.
6. Re-audit to confirm the change is complete.
7. Sync records with `sync-figma-token` if semantics changed.

### Skill Stack

- `figma-use` — inspection and targeted edits (must invoke per Child Skill Invocation Gates)
- `audit-design-system` — drift identification (must invoke per Child Skill Invocation Gates)
- `figma-generate-library` — phase and work order decisions
- `sync-figma-token` — token parity verification when source alignment matters
- `rad-spacing`, `clarify`, `normalize` — per Child Skill Invocation Gates

### Output Artifacts

- Repaired Figma governance or canonical pages
- Corrected variable, style, or component bindings
- Token parity or drift notes
- Explicit record of what changed and why

### When To Ask For Input

Stop and ask when:

- The SSOT token source is missing or disputed
- The page role is unclear between governance, canonical, and reference
- A change may alter accepted semantics rather than only fix drift
- The task could be governance work or application work and the user intent is not explicit

---

## DS Application

`DS Application` is a parent layer. Before execution, route into one of these sub-scenarios:

- `DS To Design`
- `Design To Demo`
- `Prompt To Demo`
- `DS To Code`

### Non-Negotiable DS Application Constraints

These apply to every `DS Application` sub-scenario.

#### Canonical Source Priority

The attached DS inputs are the authority for execution order and visual semantics. Do not treat DS inputs as inspiration, soft guidance, or visual reference only. If Figma, source token JSON, and the target artifact disagree, stop and determine which layer is canonical for that decision instead of blending them loosely.

#### Required Fallback Order

Apply the Incomplete DS Execution Protocol defined above. For every major region, component, and visual decision, use the deepest DS tier that is available and stop at that tier.

#### Token Discipline

- Typography family, weight, size, line height, and letter spacing must come from canonical token definitions when available.
- Radius, spacing, control heights, icon sizes, borders, fills, semantic colors, and gradients must come from canonical token definitions when available.
- Do not create a parallel local token system when the canonical DS token already exists.
- Prefer token-path-backed values over raw literals at every opportunity.

#### Hex and Literal Value Restrictions

- Avoid raw hex, rgba, or ad hoc literal values whenever a canonical DS token exists for the same purpose.
- If a literal value must be used because no canonical DS value exists, treat it as a documented exception and report it as a DS gap. Do not present it as normal token reuse.

#### Semantic Alignment Requirement

Before claiming DS application quality, compare and align:
1. DS Figma semantics
2. Source token JSON semantics
3. Target artifact semantics (including HTML structure and naming when HTML is involved)

Do not rely on visual similarity alone. Align meaning, hierarchy, state intent, and token usage across all three layers.

#### Validation Requirement

Before finalizing any `DS Application` output, verify that the major regions can be explained in terms of canonical DS components, patterns, semantic tokens, or primitive tokens. If a region cannot be explained using that chain, treat the output as incomplete DS application work and report it as such.

#### DS Application Pre-Flight Checklist

Before substantial execution begins for any `DS Application` scenario:

- [ ] Have I identified the canonical DS Figma source, the canonical source token JSON, and the intended output artifact?
- [ ] For each major region, do I know whether I am using a DS component, a DS pattern, semantic tokens, primitive tokens, or reporting a gap?
- [ ] Am I reusing canonical typography definitions instead of introducing a local font system?
- [ ] Am I reusing canonical radius, spacing, size, and color definitions instead of introducing local approximations?
- [ ] Am I avoiding raw hex, rgba, and ad hoc literal values unless confirmed no canonical DS value exists for that purpose?
- [ ] If I must use a literal fallback, have I treated it as an explicit exception and DS gap?
- [ ] If the target is HTML, code, or demo output, does the structure and naming reflect the DS semantics rather than only the visual appearance?
- [ ] Can I explain how the output aligns DS Figma semantics, source token JSON semantics, and target artifact semantics?

If the answer is no to any checklist item, stop and resolve that gap before claiming DS-backed execution quality.

---

### DS To Design

Use this mode when the user wants a Figma design created, repaired, or extended from the DS.

**Default skill invocation order** (skip a step only if explicitly not applicable, and state why):

1. `audit-design-system` — inspect and identify drift (must invoke, see gates)
2. `apply-design-system` — section-level or page-level reconnection when drift is significant (must invoke per gates when drift is found)
3. `figma-use` — contained structural edits, binding work, naming work, and validation (must invoke per gates)
4. `figma-generate-design` — if a full-page or new section must be generated from scratch (invoke per gates)
5. `rad-spacing` — when spacing and hierarchy are the main issue (invoke per gates)
6. `clarify` — when copy, labels, or state names are unclear (invoke per gates)
7. `normalize` — when conventions need unification after application (invoke per gates)

**Output artifacts:**

- Repaired or newly generated Figma design work
- DS-connected components, styles, and variable bindings in Figma
- Direct screen links or page links for review
- Explicit note on DS usage depth and remaining gaps

**Stop and ask when:**

- The target Figma page is unclear
- The design surface is too ambiguous to know what should be preserved versus replaced
- The user has not made clear whether the output should stay in Figma or become a demo
- The DS side is missing a canonical pattern needed for the requested design

---

### Design To Demo

Use this mode when the user has an existing Figma surface and wants a non-production demo generated from it.

**Default skill invocation order** (skip a step only if explicitly not applicable, and state why):

1. Inspect canonical source token JSON first to understand the active semantic layer
2. `audit-design-system` — inspect the source Figma surface and identify what is canonical versus approximate (must invoke, see gates)
3. `figma-use` — inspect component structure, assets, variables, and reusable building blocks (must invoke, see gates)
4. `apply-design-system` — if the source Figma surface itself needs bounded DS reconnection before demo generation (invoke per gates)
5. Demo implementation work using the discovered design and DS structure
6. Targeted validation using structure, screenshot, and node data
7. `rad-spacing`, `clarify`, or `normalize` — only if the generated demo needs bounded cleanup (invoke per gates)

**Output artifacts:**

- AI demo or interactive prototype
- Short note stating whether the demo is component driven, locally componentized, or mostly approximate
- Direct review links to the source Figma surface when they help explain fidelity
- Skill-Wide Delivery Report

**Stop and ask when:**

- The wrong Figma source may be selected
- The user has not made clear whether they want a demo or a Figma design
- The source design is too incomplete to know what behavior or states the demo should include
- The DS does not expose enough reusable patterns and the missing scope would force broad invention

---

### Prompt To Demo

Use this mode when a prompt, PRD, or product intent is the main source and the output is a demo or prototype.

**Important:** If the user says "demo" or "prototype" but actually wants the final artifact in Figma, re-route to `DS To Design` before execution.

**Default skill invocation order** (skip a step only if explicitly not applicable, and state why):

1. Inspect canonical source token JSON first to understand primitive and semantic constraints
2. `figma-generate-design` — DS-backed page or section generation (must invoke when output is Figma, see gates)
3. `edit-figma-design` — text-driven design iteration
4. `figma-use` — structural editing and binding (must invoke, see gates)
5. `audit-design-system` — post-generation validation (invoke per gates)
6. `apply-design-system` — if the generated surface needs stronger DS reconnection (invoke per gates)

**Generation discipline:**

- Do not start from clone-based pages as the final method unless the user explicitly asks for a fast clone-based draft.
- Prefer a component-driven build order over a frame-driven build order.
- First inventory which DS components are actually reusable in the target file or linked library.
- Separate what is truly componentized from what is only token- or style-aligned.
- If business-specific blocks do not exist as DS components, create the smallest local reusable components first, then compose screens from instances.

**The agent must explicitly distinguish these implementation depths in the delivery report:**

- visual approximation only
- token and style aligned
- component driven
- canonical DS component driven

Do not report a result as "based on the DS" without stating which of those levels was actually reached.

**Output artifacts:**

- AI demo or prototype driven by prompt and DS constraints
- Explicit note on which DS surfaces, components, and token layers were used
- Skill-Wide Delivery Report

**Stop and ask when:**

- The prompt is too vague to determine screen scope, states, or output shape
- The user has not made clear whether the final output should remain a demo or become a Figma design
- The prompt requires a business pattern not represented in the DS and would need semantic invention
- The available DS surfaces are too weak to choose a stable composition with confidence

---

### DS To Code

Only move into `DS To Code` when:

- The target surface is canonical rather than historical
- The component family has stable naming and variant axes
- Token semantics are stable enough to map to code-side usage
- The intended handoff surface can be validated without relying on governance history

**Default skill invocation order** (skip a step only if explicitly not applicable, and state why):

1. `audit-design-system` — verify canonical readiness, stable naming, and token semantics (must invoke, see gates)
2. `figma-use` — bounded Figma-side hardening when the surface is close but not yet ready (must invoke, see gates)
3. `figma-implement-design` — node-to-code translation once the surface is stable (must invoke, see gates)
4. `figma-code-connect-components` — only after the component family is stable enough for durable mapping (invoke per gates)
5. Post-handoff verification to confirm the target surface still matches the intended code boundary

**Output artifacts:**

- Production-facing implementation or handoff-ready code output
- Explicit statement of the source Figma surface used for handoff
- Mapping or fidelity notes when component families are involved
- Confidence and residual risk report for implementation readiness

**Stop and ask when:**

- The target handoff surface is not clearly canonical
- The user has not made clear whether demo quality is enough or production quality is required
- The component family is unstable enough that code mapping would be misleading
- Figma handoff constraints conflict with codebase constraints and the tradeoff is not explicit

If those conditions are not met, stop at `DS Governance` or another `DS Application` sub-scenario and do not force a code workflow.

---

## Skill-Wide Delivery Report

After any substantial execution in this skill — regardless of scenario — the agent must include a delivery report in the following fixed format.

This is required even when the task is mostly successful.

```
## Delivery Report

Scenario:        [DS Governance / DS To Design / Design To Demo / Prompt To Demo / DS To Code]
Confidence:      [High / Medium / Low] — [one-line reason]
DS depth reached: [visual approx / primitive / semantic / pattern / canonical component]

High-confidence areas:
- [area]: [reason — e.g., "uses canonical Button component from DS library"]
- ...

Low-confidence / approximate areas:
- [area]: [reason — e.g., "no semantic token for this border; used primitive gray.800 approximation"]
- ...

DS gaps found:
- [gap]: [what was missing and what tier was used as fallback]
- [none] if no gaps found

Source agreement:
- Figma ↔ source token JSON: [aligned / partial / conflict — brief note]
- Output ↔ source token JSON: [aligned / partial / conflict — brief note]
- Screenshot ↔ node data: [aligned / mismatch — brief note if applicable]

Next input needed:
- [what the user should provide next to get a tighter result, or "none" if the run is complete]
```

### When the run writes to Figma, also include

```
Figma output:
- Build method: [clone-based / primitive-built / locally componentized / library-componentized]
- Review surface: [section link / screen link / node ID]
- Validation basis: [metadata only / screenshot only / both]
```

### Confidence tie-to-facts rule

Confidence must be backed by at least one concrete reason from this list:

- exact canonical component match exists or does not exist
- token source is complete or incomplete for the task
- required Figma surface exists or does not exist
- output was built from real DS assets versus structural approximation
- design brief is specific or underspecified
- Figma screenshot output matches node data or does not match

Do not report a vague feeling. Tie confidence to a fact.

---

## Stuck State Protocol

If the agent cannot proceed for any reason — unclear intent, missing DS layer, conflicting sources, ambiguous output surface, failed validation, or blocked tool — the agent must follow this escalation protocol instead of guessing, retrying, or silently skipping.

### Escalation Steps

1. **State the blocker clearly.**
   One sentence: "I am stuck because [specific reason]."

2. **Identify the stuck type.**
   Choose one:
   - `DS gap` — a required DS layer does not exist
   - `Intent gap` — the user's request is too vague to proceed safely
   - `Source conflict` — Figma, source token JSON, and target artifact disagree and the canonical layer is unclear
   - `Permission blocker` — a required hard trigger fired and confirmation is needed before proceeding
   - `Skill missing` — a required child skill is not installed or available

3. **State what is already done.**
   List steps completed so far so the user does not lose progress context.

4. **State the minimum input needed to unblock.**
   Be specific. Do not ask open-ended questions. Ask for exactly what is needed:
   - "Please confirm which of these two scenarios you want: [A] or [B]."
   - "The DS is missing a semantic token for [X]. Should I use [nearest primitive] or wait until the DS is updated?"
   - "Please install [skill name] before I can continue."

5. **Offer a safe partial result if one exists.**
   If work completed before the blocker is still useful, offer to deliver it now so the user has something to review while the gap is resolved.

Do not bypass the stuck state by making assumptions. Do not proceed silently past a blocker. Surface it and wait.

---

## Validation Rules

After meaningful Figma generation or write-back work, validate in this order when possible:

1. **Metadata validation** — nodes were created where expected, parent-child structure is correct, section or frame bounds actually contain the generated nodes, component instances are present rather than only frames and text
2. **Screenshot validation** — result is visually present and not clipped or off-screen, dark or light mode is actually applied, spacing and hierarchy are legible, the link the user will open lands on a readable surface
3. **Targeted node-data validation** — critical CTA text, important titles or state labels, component properties that may not render reliably in screenshots, variable mode or binding values when appearance alone is ambiguous

If validation finds a mismatch between file data and screenshot:

- Do not silently choose one source as truth
- Report the inconsistency
- Tell the user which side appears correct
- Continue only with bounded fixes

---

## Multi-Page Handling

When multiple pages are involved:

- Classify each page as canonical, reference, governance, or target before any edits
- Do not apply broad DS changes across pages until page roles are clear
- Batch work only when the page family, DS pattern, and ownership boundaries are stable
- Prefer page-by-page containment over broad file-wide rewrites
- Re-audit each target page after application rather than assuming consistency

Skill invocations per Child Skill Invocation Gates apply here without exception.

---

## Operating Rules

- Keep SSOT token files as the formal record of accepted semantics
- Use adapter JSON only when source structure needs transformation
- Prefer component inventory before generation whenever the target file may already contain reusable local or library-backed components
- If using a section as the review surface, verify that the section bounds actually enclose the generated content before sending the user the link

### Canonical Surfaces

- Foundations pages: token-facing surfaces and DS foundations
- Governance pages: cleanup lineage, migration evidence, and review references
- Canonical component pages: primary edit surface for component definition, example curation, and handoff

Prefer canonical component pages for active work. Treat governance pages as references unless the task explicitly targets governance history.

---

## Problem Handling

### When page role is unclear

- Do not assume the page is canonical
- Work on the smallest contained section
- Note the ambiguity and recommend canonization if needed

### When token sources conflict

- Identify the active SSOT before expanding the change
- Do not update multiple token sources as if they are equally canonical

### When drift is visible but the replacement is uncertain

- Report the issue
- Avoid speculative swaps
- Prefer audit output over forced remediation

### When variable bindings are inconsistent

- Repair the smallest broken binding set first
- Avoid broad token rewrites without parity review

### When required skills are missing

- Stop the workflow
- Explain which skill is missing and why it is needed
- Ask the user to install it before proceeding

### When required inputs are missing

- Stop the workflow
- Explain which input is missing and why it is needed
- Ask the user to provide it before proceeding

---

## Skill Composition

This skill is a coordinator, not a replacement for the underlying skills.

- The top-level skill sets mission, routing, and sequencing
- Required skills provide execution (gates in Child Skill Invocation Gates apply)
- Optional skills handle special cases (gates in Child Skill Invocation Gates apply)
- Mature-family skills are only for stable contracts

---

## Success Criteria

- Figma DS integrity is maintained.
- Canonical pages are clearly separated from governance pages.
- Tokens are bound instead of hard-coded wherever practical.
- Designers can find and reuse the right component without guesswork.
- Stable DS surfaces exist for AI to hi-fi prototype.
- Stable DS surfaces exist for AI to code.
- Code handoff surfaces are not tied to historical cleanup pages.
- `DS To Design` work can be applied to component-level content, including color, string, dimension, and font-style alignment.
- `Prompt To Demo` can produce DS-backed demos from user intent alone, with validation after generation.
- Demo-oriented outputs use the DS in a concrete way, not only by visual approximation.
- When component reuse is not available, the fallback is the 5-tier Incomplete DS Execution Protocol rather than silent invention.
- The user receives a Skill-Wide Delivery Report in fixed format after every meaningful execution run.
- When the agent is stuck, it surfaces the blocker immediately using the Stuck State Protocol instead of guessing or silently skipping.

## References
