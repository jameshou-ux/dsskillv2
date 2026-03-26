# Figma DS Phase 1 and Phase 2 Review

Date: 2026-03-25

Target Figma file:
`DBQdb8ymhIfTPS9GmcTqaR`

## Scope

This pass covered:

- Phase 1: component API cleanup for naming, variant schema readability, and high-confidence property naming fixes
- Phase 2: style governance audit for text styles, paint styles, and effect styles

This pass did **not** attempt a broad component rebuild or aggressive auto-layout rewiring.

## Phase 1 Changes Applied

### Variant axis and variant value cleanup

- `Nav`
  - `Property 1` -> `Variant`
  - variants:
    - `Variant=Default`
    - `Variant=Token main scroll`
- `Token list`
  - `Property 1` -> `State`
  - variants:
    - `State=Default`
    - `State=Expanded`
- `Menu`
  - `Property 1` -> `Status`
  - variants:
    - `Status=Not signed in`
    - `Status=Signed in`
- `Mobile nav`
  - retained axis `Level`
  - variants:
    - `Level=Top nav`
    - `Level=Secondary nav`
- `Breadcrumb`
  - typo fixed:
    - `Hiearachy` -> `Hierarchy`
  - variants:
    - `Hierarchy=L2`
    - `Hierarchy=L3`
    - `Hierarchy=L4`

### Boolean property naming cleanup

- `Nav`
  - `Show scan#7323:0` -> `Show Scan#7323:0`
- `Menu`
  - `Upgrade tips#636:0` -> `Show upgrade tip#636:0`
- `Mobile nav`
  - `Token bar#809:0` -> `Show token bar#809:0`
  - `Show Nav menu#809:1` -> `Show nav menu#809:1`
- `Button-Web`
  - `Blur#480:0` -> `Show blur#480:0`
  - `Description#6806:1` -> `Show description#6806:1`
- `Modal`
  - public property API redesigned
  - current exposed properties:
    - `Show title`
    - `Title text`
    - `Body text`
    - `Dialog title`
    - `Dialog subtitle`
    - `Fee label`
    - `Fee primary amount`
    - `Fee secondary amount`
    - `Alert text`
    - `Tour eyebrow`
    - `Tour step counter`
    - `Tour title`
    - `Tour body`
    - `Variant`
    - `Platform`
  - removed stale unused text properties that were no longer referenced by any node

## Phase 1 Intentionally Deferred

These were left for review instead of being force-cleaned automatically:

- `Bkg`, `Toggle`, and some screen-sized component roots
  - not converted to auto-layout just because the root frame is non-auto-layout
  - for these families, non-auto-layout is structurally acceptable and forcing auto-layout would risk visual regressions
- deep internal frame names
  - internal child names like `Frame 2087326...` were not globally renamed in this pass
  - they are lower priority than public component API and token/style correctness

## Phase 2 Audit Result

### Text styles

Current local text styles: `10`

Canonical set:

- `heroTitle`
- `heroAmount`
- `sectionLead`
- `navTitle`
- `bodyPrimary`
- `actionLabel`
- `bodySecondary`
- `sectionTitle`
- `supportingText`
- `tabLabel`

Result:

- the current Figma text style set already matches the semantic font token model in `source_token_v5.json`
- no duplicate or obviously conflicting local text styles were found in the current DS page workflow
- no text style write changes were required in this phase

### Paint styles

Current local paint styles: `10`

Gradient styles:

- `Light/gradient/general`
- `Dark/gradient/general`
- `Light/gradient/main`
- `Dark/gradient/main`
- `Light/gradient/xaut_card`
- `Dark/gradient/xaut_card`
- `Light/gradient/bar_backdrop`
- `Dark/gradient/bar_backdrop`

Component-specific styles:

- `component/button/primary/fill`
- `component/button/primary/stroke`

Result:

- gradient style coverage is sufficient for the current DS surface model
- no obvious duplicate gradients were found
- button primary styles remain justified as component-specific paint styles for now

### Effect styles

Current local effect styles: `4`

- `shadow/sm`
- `shadow/md`
- `shadow/lg`
- `shadow/xl`

Result:

- the shadow scale is clean and already governance-friendly
- no additional effect style normalization was required in this phase

## Recommended Review Focus

Please review these in Figma:

1. component property panel readability for:
   - `Nav`
   - `Token list`
   - `Menu`
   - `Mobile nav`
   - `Breadcrumb`
   - `Button-Web`
   - `Modal`
2. whether `component/button/primary/fill` and `component/button/primary/stroke` should remain as component paint styles or be re-expressed another way

## Recommendation For Next Implementation Pass

If this review is approved, the next write pass should be:

1. selectively rename high-value internal frames and slots for maintainability
2. decide whether `Pattern` / `Component` collections should be reduced further
3. expand the same audit to non-core pages and detached showcase examples
