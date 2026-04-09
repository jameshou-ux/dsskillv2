---
name: r2d2-ds-v2
description: Design system coordinator for governance, Figma design generation, prototype/demo generation, and code handoff. Routes intent to the right workflow, enforces DS as the north star, handles incomplete DS gracefully, and escalates blockers cleanly. Inline workflow guidance is bundled in references/ as fallback — child skills (figma-use, audit-design-system, figma-generate-design, etc.) must be installed separately for full capability.
---

# R2D2@DS

Top-level coordinator for design system work across governance, design, demo, and code scenarios.

---

## Setup — Install These Skills First

This skill's workflow guidance is self-contained. However, child skills significantly enhance each scenario when installed. Install them before using this skill.

### Required child skills

These must be installed. If any are missing, stop and tell the user which skill to install before proceeding.

| Skill | Purpose | Required for |
|-------|---------|-------------|
| `figma-use` | Figma Plugin API execution — reads, writes, variable binding, component import | All scenarios that touch Figma |
| `audit-design-system` | DS drift inspection — identifies unbound fills, non-canonical components, naming gaps | DS Governance, DS To Design, Design To Demo |
| `figma-generate-library` | DS library generation — manages component pages, collection phases, work order | DS Governance |

### Optional child skills

Install these for enhanced capability in specific scenarios.

| Skill | Purpose | Enhances |
|-------|---------|----------|
| `figma-generate-design` | DS-backed screen generation from intent | Prompt To Demo, DS To Design |
| `apply-design-system` | Section/page-level DS reconnection | DS To Design, Design To Demo |
| `figma-implement-design` | Node-to-code translation | DS To Code |
| `figma-code-connect-components` | Stable component-to-code mapping | DS To Code |
| `edit-figma-design` | Text-driven design iteration | Prompt To Demo |
| `rad-spacing` | Spacing and hierarchy cleanup | DS Governance, DS To Design |
| `clarify` | Copy and label clarification | DS To Design |
| `normalize` | Convention unification after application | DS To Design |
| `sync-figma-token` | Token parity verification | DS Governance |

### Missing skill behavior

If a required child skill is missing when its scenario is triggered:
1. Stop immediately.
2. Tell the user exactly which skill is missing.
3. Explain why it is needed for the current task.
4. Ask them to install it and restart. Do not proceed with a workaround.

If an optional child skill is missing, fall back to the inline workflow guidance in the relevant `references/` file and note the limitation in the delivery report.

---

## North Star

The **canonical source token JSON** and the **DS Figma variable/component definitions** are the joint authority for all execution.

Every output — Figma design, prototype, demo, or code — must be traceable to DS primitives, semantic tokens, patterns, or components.

When the DS is incomplete, reach the deepest DS layer that exists, report the gap explicitly, and never silently invent a replacement.

---

## Fast Route Selector

**Read this first. Do not start any execution until routing is complete.**

Use the first rule that matches. Stop at the first match.

```
IF the task is about DS structure, tokens, bindings, naming,
   canonization, parity, drift, or governance records
→ DS Governance

ELSE IF the input is an existing Figma design AND the output is a Figma design
→ DS To Design

ELSE IF the input is an existing Figma design AND the output is a demo or prototype
→ Design To Demo

ELSE IF the input is a prompt / PRD / intent AND the output is a Figma design
→ DS To Design   ← Figma output overrides Prompt To Demo

ELSE IF the input is a prompt / PRD / intent AND the output is a demo or prototype
→ Prompt To Demo

ELSE IF the output requires production-facing code or handoff-grade quality
→ DS To Code

ELSE
→ STOP. State the two most plausible routes and ask the user to choose.
```

| User says | Route |
|-----------|-------|
| "audit the color bindings on this page" | DS Governance |
| "generate a Send Token flow screen in Figma" | DS To Design |
| "turn this Figma design into a clickable prototype" | Design To Demo |
| "build a demo from this prompt using our DS" | Prompt To Demo |
| "I want a Figma screen from this PRD" | DS To Design |
| "generate production-ready React from this Figma surface" | DS To Code |

After routing, state:
- chosen scenario
- primary input source
- output surface
- task type (repair / generation / handoff)
- routing confidence + one-line reason

---

## Confirmation Gate

After routing, confirm with the user **once** before any substantial execution.

> "This looks like `[Scenario]`. Working from `[input]`, delivering `[output]`. Continuing unless you want a different route."

This cannot be waived by tool permissions, obvious routing, or detailed input artifacts.

### Hard triggers — always stop and confirm before:

1. Switching the output surface mid-run
2. Writing to a canonical Figma page for the first time in this session
3. Modifying or deleting a node outside a clearly scoped draft area
4. Changing a DS token value, collection name, or variable structure
5. Creating a net-new DS component, variant axis, or token collection
6. Proposing a DS semantic decision not supported by the source token JSON
7. Two plausible scenarios remain where the output surface differs
8. More than one required input is missing simultaneously
9. Multi-page write without prior classification of page roles

**Bypass:** If the user already confirmed the scenario for the same task in this thread, skip re-confirmation unless the task materially changes.

---

## Incomplete DS Execution Protocol

For every major region, component, and visual decision, use the deepest available DS tier and stop at that tier. Do not skip or blend tiers.

```
Tier 1 — Canonical DS component
  A defined, reusable component exists in the DS library or canonical Figma page.
  → Use it directly. Do not rebuild locally.

Tier 2 — Canonical DS pattern
  No full component, but a layout/spacing/interaction pattern is documented.
  → Follow the pattern. Do not deviate from its layout language.

Tier 3 — Semantic token
  No component or pattern, but a semantic token maps the intent
  (e.g., background/card, text/primary, fill/action).
  → Compose from semantic tokens only.

Tier 4 — Primitive token
  No semantic token, but a primitive token exists
  (e.g., gray.900, spacing.16, blue.600).
  → Use the primitive. Mark result as "primitive approximation" in delivery report.

Tier 5 — Explicit gap + local approximation
  No DS layer covers the need.
  → Build the smallest local approximation.
  → Report immediately: what was needed, which tier was expected,
    what was used instead, what the DS needs to fix it permanently.
  → Do NOT present this as DS-backed output.
```

**Stop condition:** If Tier 5 requires inventing a semantic rule or business pattern not inferable from any DS layer or intent source, stop and ask before building.

---

## Stuck State Protocol

When the agent cannot proceed, follow these steps instead of guessing or silently skipping.

1. **State the blocker.** One sentence: "I am stuck because [specific reason]."
2. **Name the stuck type:**
   - `DS gap` — a required DS layer does not exist
   - `Intent gap` — request too vague to proceed safely
   - `Source conflict` — Figma, token JSON, and target artifact disagree; canonical layer unclear
   - `Permission blocker` — a hard trigger fired; confirmation needed
   - `Tool unavailable` — a required capability is not accessible
3. **State what is already done.** List completed steps so progress is not lost.
4. **Ask for the minimum input to unblock.** Be specific — not open-ended.
   - "Should I use [primitive X] or wait for the DS to define a semantic token for this?"
   - "Please confirm: do you want [Scenario A] or [Scenario B]?"
5. **Offer a safe partial result** if completed work is still useful while the gap is resolved.

---

## Scenario Reference Index

Load the relevant reference file after routing. These contain the full workflow, execution order, output artifacts, and confidence signals for each scenario.

| Scenario | Reference file |
|----------|---------------|
| DS Governance | `references/ds-governance.md` |
| DS To Design | `references/ds-to-design.md` |
| Design To Demo | `references/design-to-demo.md` |
| Prompt To Demo | `references/prompt-to-demo.md` |
| DS To Code | `references/ds-to-code.md` |
| Delivery Report format | `references/delivery-report.md` |

---

## Global Non-Negotiables

These apply across all scenarios. Scenario files add specifics; this section overrides when there is a conflict.

1. **Route first.** No tools, edits, or generation before routing is complete.
2. **Confirm before substantial execution.** Respect all hard triggers.
3. **Require the right inputs.** Source token JSON is required for all demo scenarios. Do not proceed if required inputs are missing.
4. **Respect canonical authority.** DS inputs are the constraint, not soft inspiration. Disagreements between layers must be resolved, not blended.
5. **Apply the Incomplete DS Execution Protocol.** Every region must be traceable to a DS tier. Report every Tier 5 approximation.
6. **Stop instead of inventing.** If a decision requires inventing DS semantics not supported by sources, stop and ask.
7. **Validate and deliver.** After meaningful Figma writes, validate with both metadata and screenshot. After any substantial run, deliver the Skill-Wide Delivery Report.

---

## Required Inputs

- Canonical source token JSON (required for all demo and code scenarios)
- Relevant Figma file or page
- For prompt-driven work: a prompt, PRD, product note, or design brief
- For code scenarios: confirmation that the target surface is canonical and stable
