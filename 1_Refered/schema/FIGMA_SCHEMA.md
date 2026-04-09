# FIGMA_SCHEMA.md

## Purpose

This document defines how a detailed `DESIGN.md` should be interpreted when building, normalizing, or updating a Figma design system.

It exists to bridge the gap between:

- design language and rules in `DESIGN.md`
- Figma variables, styles, components, and patterns
- AI/agent workflows that write to or maintain a Figma library

`DESIGN.md` is the design-language specification.  
`FIGMA_SCHEMA.md` is the Figma modeling specification.

This document is intended to support:

- Figma variable generation
- text style and effect style setup
- component set construction
- variant and property modeling
- page-level normalization before AI-to-code handoff
- AI-assisted writeback into Figma libraries

For this repo, token naming must remain consistent with the approved token source file, currently [source_token_v5.json](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/2026-03-25/source_token_v5.json).

---

## Source Hierarchy

When information conflicts, resolve in this order:

1. Approved Figma component schema in this document
2. Approved Figma design system library
3. Approved `DESIGN.md`
4. Screen-level Figma files
5. AI inference

Rule:
AI may infer only when layers 1-4 do not provide enough information.

---

## Token Naming And Hierarchy

Token naming must follow the approved source token hierarchy, not ad hoc names invented during Figma generation.

Current approved token hierarchy:

- `Primitive.primitive.*`
- `Light.semantic.*`
- `Light.pattern.*`
- `Dark.semantic.*`
- `Dark.pattern.*`

Use this hierarchy as authoritative for token references and Figma variable grouping.

### Primitive Token Groups

Under `Primitive.primitive.*`, use the existing groups:

- `color`
- `spacing`
- `size`
- `radius`
- `typography`

Examples:

- `Primitive.primitive.color.blue.500`
- `Primitive.primitive.color.navy.900`
- `Primitive.primitive.spacing.16`
- `Primitive.primitive.size.48`
- `Primitive.primitive.radius.md`
- `Primitive.primitive.typography.family.sans`
- `Primitive.primitive.typography.size.lg`

### Mode-Specific Semantic Token Groups

Use mode-specific semantic groups rather than generic invented aliases.

Examples:

- `Light.semantic.background.card`
- `Light.semantic.text.primary`
- `Light.semantic.fill.action`
- `Light.semantic.border.default`
- `Light.semantic.font.actionLabel`
- `Dark.semantic.background.card`
- `Dark.semantic.text.inverse`
- `Dark.semantic.stroke.icon_primary`

### Pattern Token Groups

Pattern-level tokens must remain under the approved mode-specific `pattern` branches.

Examples:

- `Light.pattern.surface.card.background`
- `Light.pattern.surface.card.radius`
- `Dark.pattern.surface.card.background`

### Naming Rules

- Preserve the existing token branch names from the token source.
- Do not rename token families inside Figma to match generic schema language.
- Do not introduce new token aliases when an approved token already exists.
- If a needed token does not exist, propose it against the token source instead of inventing a Figma-only variable.

Rule:

- Layer naming in Figma may be recommended by this schema.
- Component property naming in Figma may be recommended by this schema.
- Token naming must stay consistent with the approved token source.

---

## Modeling Layers

Every reusable design object must be classified into one of the following layers.

### Primitive

Definition:
A single-purpose UI element with stable semantics and high reuse.

Examples:

- `Button`
- `Input`
- `Badge`
- `Avatar`
- `IconButton`
- `Chip`
- `NavItem`

Use when:

- the object has a clear standalone semantic role
- the object is reused widely across screens
- designers are expected to place it directly

### Composite

Definition:
A reusable composition of primitives with stable structure and bounded use cases.

Examples:

- `SearchBar`
- `AssetRow`
- `StepCard`
- `HoldingCard`
- `EmptyStateCard`

Use when:

- the object contains multiple primitives
- its structure is stable
- it is reusable but not foundational

### Pattern

Definition:
A reusable screen-level block or section composed of primitives and composites. It is reused across flows, but is too contextual to belong in the primitive library.

Examples:

- `PortfolioSummarySection`
- `ActionBarSection`
- `TradingTaskSection`
- `OnboardingStepSection`
- `HeroSection`

Use when:

- the object represents a block of a page, not a base component
- it carries domain meaning
- it is reused across multiple screens or flows

### Page

Definition:
A route-level or screen-level composition. Not a reusable design system asset.

Examples:

- `Home`
- `TokenPortfolio`
- `CrossChainSend`
- `AgentTrading`
- `KeylessOnboarding`

Rule:

- Do not model a Pattern as a Primitive.
- Do not model a Page as a library component.

---

## Variant Eligibility Rules

A difference may be modeled as a variant only if all of the following are true:

- it is the same semantic object
- the base structure is substantially the same
- the interaction model is the same
- the content model is the same
- the difference is expected to be designer-selectable in routine use

### Good Variant Axes

- `Hierarchy`
- `State`
- `Size`
- `Tone`
- `Density`
- `Emphasis`
- `Selection`
- `Icon`

### Bad Variant Candidates

- radically different layout
- floating vs inline placement behavior
- different interaction role
- screen-specific business composition
- large structural changes
- differences that create a different designer mental model

Rule:

- If the semantic role changes, split component.
- If the layout behavior changes materially, split component.
- If the page usage role changes materially, create a separate component or a Pattern.

Example:

- `Button` and `FloatingButton` must not be the same component family.

---

## Split Component Rules

Create a separate component instead of adding another variant when one or more of the following are true:

- structure changes by more than minor slot differences
- layout mode changes in a fundamental way
- page placement role changes
- designer usage intent changes
- property panel would become confusing
- state matrix becomes too large to reason about
- the component would exceed four primary variant axes in normal use

Examples:

- `Button` and `FloatingButton`
- `Card` and `SectionPanel`
- `Badge` and `Chip`
- `InlineLink` and `Button`

Rule:

- Prefer two clear components over one overloaded component set.

---

## Pattern Eligibility Rules

Model an object as a Pattern when all or most of the following are true:

- it is composed of multiple primitives or composites
- it is reused across screens or flows
- it is not generic enough to belong in the primitive library
- it carries domain-level meaning
- it requires bounded but not universal reuse

Examples:

- `PortfolioAssetSection`
- `TradingAgentTaskPanel`
- `OnboardingChecklistSection`

Do not model an object as a Pattern when:

- it is only used once
- it is only a page layout artifact
- it should actually be a Composite

Rule:

- Patterns may live in a separate Figma page or separate library section.
- Patterns must not pollute primitive foundations.

---

## Property Design Rules

Property names must use design semantics, not engineering internals.

### Preferred Property Names

- `Hierarchy`
- `State`
- `Size`
- `Tone`
- `Icon`
- `Selection`
- `Emphasis`
- `Density`

### Avoid

- `variant`
- `intent`
- `type2`
- `modeA`
- implementation-specific prop names unless explicitly standardized by the team

### Property Rules

- Use Variant properties for mutually exclusive design families.
- Use Boolean properties for simple toggles.
- Use Text properties for labels and editable copy.
- Use Instance swap for icons and nested subcomponent slots.

Rule:

- Do not expose a property unless a designer is likely to use it directly.
- Property names are recommendations for Figma usability and may differ from code prop names.

---

## Recommended Property Types

### Use Variant Property For

- hierarchy family
- size family
- explicit state demos
- layout family when still the same semantic object

### Use Boolean Property For

- `Has Leading Icon`
- `Has Trailing Icon`
- `Selected`
- `Loading`
- `Has Subtitle`
- `Has Helper Text`

### Use Text Property For

- `Label`
- `SupportingText`
- `Count`
- `BadgeValue`
- `HelperText`

### Use Instance Swap For

- `LeadingIcon`
- `TrailingIcon`
- `Avatar`
- `Media`
- nested approved subcomponents

Rule:

- Prefer fewer, clearer properties over exhaustive parameterization.

---

## State Modeling Rules

Only include states as selectable variants when they are useful in routine design workflows.

### States That Usually Belong In The Main Component Set

- `Default`
- `Hover`
- `Pressed` or `Active`
- `Disabled`

### States To Use With Restraint

- `Focus`
- `Loading`
- `Error`
- `Success`

Rule:

- Not every engineering state must be a Figma property.
- If a state is mainly documentation, represent it in examples or demo frames rather than the main property panel.

---

## Slot Modeling Rules

Every reusable component may define named slots.

### Allowed Slot Types

- `Label`
- `SupportingText`
- `LeadingIcon`
- `TrailingIcon`
- `Avatar`
- `Media`
- `Action`
- `Badge`

### Slot Rules

- Slot names must be stable across similar components.
- Slots should map to clear layer names.
- Deep hidden slots should not be exposed unless necessary.
- Icons should use instance swap when possible.
- Text should use text properties when possible.

Rule:

- If slot behavior differs fundamentally between cases, reconsider whether those cases belong in the same component.

---

## Layer Naming Rules

Use semantic, predictable layer names.

### Top-Level Page Naming

- `Page/Home`
- `Page/Token Portfolio`

### Section Naming

- `Section/Hero`
- `Section/Portfolio Summary`
- `Section/Action Grid`

### Component Instance Naming

- `Component/Button`
- `Component/Card`
- `Component/Badge`

### Slot Naming

- `Slot/Label`
- `Slot/LeadingIcon`
- `Slot/SupportingText`
- `Slot/Action`

### Custom One-Off Naming

- `Custom/OneOff`
- `Custom/PageOnly`

### Candidate Naming

- `Candidate/AssetCard`
- `Candidate/FloatingActionEntry`

Rule:

- Do not require every internal layer to be perfectly named.
- Do require top-level containers, component instances, and key slots to follow naming rules.

---

## Variable Binding Rules

Where possible, Figma components must bind to approved variables for:

- color
- spacing
- radius
- stroke
- effect tokens where supported
- typography styles or mapped text styles

Binding references in Figma documentation, AI prompts, and schema mappings must point to the approved token hierarchy from the token source file.

### Preferred Binding Style

When describing bindings, use explicit source-token paths such as:

- `Primitive.primitive.color.blue.500`
- `Primitive.primitive.radius.full`
- `Primitive.primitive.spacing.16`
- `Light.semantic.fill.action`
- `Light.semantic.font.actionLabel`
- `Dark.semantic.background.card`

Avoid generic references such as:

- `color.interactive.primary`
- `radius.full`
- `text.primary.onBrand`

Rule:

- Local ad hoc values are allowed only in exploration files, not in approved library assets.

---

## AI Read and Write Rules

AI may do automatically:

- bind variables to matching library components
- normalize names
- replace obvious one-off nodes with approved components
- update variants when mapping is unambiguous
- create Pattern blocks from approved compositions
- flag detached instances, custom blocks, and candidate components

AI must ask for approval or create a proposal when:

- adding a new Primitive component
- adding a new variant axis
- renaming a public property
- splitting an existing component family
- merging two existing component families
- changing Pattern vs Primitive classification

Rule:

- AI executes library maintenance.
- Humans decide taxonomy changes.

---

## Mapping From DESIGN.md

Interpret `DESIGN.md` in this order:

1. Extract the design object
2. Determine the modeling layer
3. Determine allowed variant axes
4. Determine disallowed axes
5. Determine slots
6. Determine variable bindings

### Example Interpretation Process

Input from `DESIGN.md`:

- "Primary button"
- "Outline button"
- "Hero CTA"

Interpretation:

- Design object: `Button`
- Modeling layer: `Primitive`
- Allowed axes: `Hierarchy`, `Size`, `State`
- Disallowed axes: page placement, floating behavior, section-specific layout
- Slots: `Label`, optional `LeadingIcon`, optional `TrailingIcon`
- Variable bindings:
  - light primary fill -> `Light.semantic.fill.action`
  - light label text -> `Light.semantic.text.inverse`
  - dark primary fill -> `Dark.semantic.fill.action`
  - radius -> `Primitive.primitive.radius.full`
  - height and paddings -> `Primitive.primitive.size.*` and `Primitive.primitive.spacing.*`
  - text style -> `Light.semantic.font.actionLabel` / `Dark.semantic.font.actionLabel`

Rule:

- `DESIGN.md` defines design semantics.
- This schema defines Figma modeling decisions.

---

## Example Modeling Decisions

### Button

Layer:

- `Primitive`

Allowed variant axes:

- `Hierarchy = Primary | Secondary | Outline | Ghost | Link`
- `Size = sm | md | lg | hero`
- `State = Default | Hover | Active | Disabled`

Allowed booleans:

- `Has Leading Icon`
- `Has Trailing Icon`

Text properties:

- `Label`

Preferred token bindings:

- fill -> `Light.semantic.fill.action` / `Dark.semantic.fill.action`
- text -> `Light.semantic.text.inverse` / `Dark.semantic.text.inverse`
- radius -> `Primitive.primitive.radius.full`
- typography -> `Light.semantic.font.actionLabel` / `Dark.semantic.font.actionLabel`

Not included:

- `Floating`
- `Sticky Bottom CTA`

Reason:

- These change placement behavior and design intent and must not be modeled as standard Button variants.

### FloatingButton

Layer:

- `Primitive` or `Composite`, depending on system scope

Why not a Button variant:

- different placement behavior
- different usage role
- often different content structure
- different designer mental model

### HoldingCard

Layer:

- `Composite`

Reason:

- Stable reusable composition of existing primitives from the alpha design spec.

### PortfolioSummarySection

Layer:

- `Pattern`

Reason:

- Section-level reusable block, too contextual for primitive library.

---

## Library Structure Guidance

Recommended top-level Figma design system organization:

- `00 Foundations`
- `01 Primitives`
- `02 Composites`
- `03 Patterns`
- `04 Templates or Screens`
- `99 Playground`

### Foundations

Include:

- variables
- text styles
- effect styles
- icon references
- spacing and radius references

### Primitives

Include:

- base interactive elements
- form controls
- small reusable UI atoms

### Composites

Include:

- reusable cards
- rows
- grouped input patterns
- richer but bounded reusable modules

### Patterns

Include:

- section-level reusable business blocks

### Templates or Screens

Include:

- reference compositions only
- not part of the strict reusable library

### Playground

Include:

- experiments
- incoming candidate components
- cleanup and staging work

Rule:

- Exploration and approved library assets must not live in the same place without clear separation.

---

## Agent Workflow For Figma Import And Normalization

This schema is designed to enable AI or agent workflows that convert a detailed `DESIGN.md` into Figma-ready variables, styles, and bound components.

### Step 1: Read DESIGN.md

Agent extracts:

- color roles
- typography hierarchy
- spacing and radius scale
- motion and effect definitions
- component families
- variant candidates
- responsive and layout rules

### Step 2: Create Foundations

Agent creates or updates:

- color variables
- semantic variables
- light and dark mode values
- text styles
- effect styles where practical

Rule:

- Variable collection and naming should mirror the token source hierarchy as closely as Figma allows.
- Do not flatten or rename token groups unless there is a Figma-specific technical limitation.

### Step 3: Model Components

Agent classifies each design object as:

- `Primitive`
- `Composite`
- `Pattern`

Then:

- creates component sets
- creates or updates variant properties
- binds variables
- applies slot naming conventions

### Step 4: Normalize Existing Figma Assets

Agent may:

- detect detached instances
- detect obvious one-off frames
- replace eligible one-offs with approved component instances
- flag candidate components for approval
- normalize top-level names and sections

### Step 5: Write Back To Library

After approval, agent may:

- promote approved candidates into component sets
- update property structures
- move assets into the correct library page
- align naming and bindings

Rule:

- Agents may automate build and normalization.
- Taxonomy changes must be reviewable and approved.

---

## Minimum Approval Gates

The following actions require explicit review before library writeback:

- new Primitive component
- new variant axis
- split of an existing component family
- merge of existing component families
- reclassification from Composite to Primitive
- reclassification from Pattern to Composite
- public property rename

The following actions may be auto-applied:

- variable binding corrections
- text style normalization
- obvious one-off replacement with approved component
- name normalization under approved naming rules
- movement of assets to the correct approved page

---

## MVP Governance Checklist

Before approving a new Figma component, confirm:

- semantic object is clear
- correct modeling layer is chosen
- variant family is not overloaded
- property names are design-facing
- slot names are stable
- key variables are bound
- designers can use it without editing internals
- this should be reusable, not page-only
- code mapping is plausible
- AI can safely identify it later

---

## Standalone Output Expectations

When an agent uses this schema together with a detailed `DESIGN.md`, the expected outputs are:

- Figma variable collections
- light and dark mode bindings
- text styles
- effect styles where practical
- component sets with clean variant axes
- stable property names
- normalized slot naming
- separated Primitive, Composite, and Pattern layers
- handoff-ready pages that are more machine-readable

This document should be used as the Figma-side modeling contract for AI-assisted design system generation and maintenance.

---

## Repo-Specific Notes For Alpha

This schema is currently expected to work with:

- [alpha design.md](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/design%20md/alpha%20design.md)
- [source_token_v5.json](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/2026-03-25/source_token_v5.json)

For this repo:

- component names such as `Button`, `IconButton`, `ActionButton`, `Badge`, `Avatar`, `Card`, `SectionPanel`, `Chip`, `Input`, `Progress`, `NavItem`, `StepCard`, `AssetRow`, `HoldingCard`, `TaskCard`, and `ChecklistCard` should be preferred over generic substitutes when matching `DESIGN.md`
- token references must use the source token naming hierarchy
- Figma layer naming remains a recommended schema layer, not the token source of truth
- Figma component property naming remains a recommended schema layer, not the token source of truth
