# DS To Design — Full Workflow

Use this scenario when the user wants a Figma design created, repaired, or extended from the DS.

## Child Skills for This Scenario

| Skill | Role | Required? |
|-------|------|-----------|
| `figma-use` | Figma reads, writes, variable binding, component import | Required |
| `audit-design-system` | Inspect current surface and identify drift before applying DS | Required |
| `apply-design-system` | Section/page-level DS reconnection when drift is significant | Optional |
| `figma-generate-design` | Full-page or multi-section generation from scratch | Optional |
| `rad-spacing` | Spacing and hierarchy cleanup | Optional |
| `clarify` | Copy and label clarification | Optional |
| `normalize` | Convention unification after application | Optional |

If `figma-use` or `audit-design-system` are not installed, stop and tell the user to install them before proceeding. For optional skills, fall back to the inline workflow below and note the limitation in the delivery report.

Focus: bring a design surface in Figma into a real DS-backed state using variable bindings, canonical components, and DS-defined tokens.

If the current agent cannot write to Figma, stop and ask the user to switch to a Figma-capable agent or to re-route the task to a demo scenario. Do not simulate completion with HTML, screenshots, or prose and call it DS To Design.

---

## Required Inputs

- Canonical source token JSON
- Target Figma file and page
- If repairing an existing design: the existing Figma page URL or node ID
- Live Figma write capability in the current agent session

---

## Execution Order

A step may be skipped only if explicitly not applicable — state why before skipping.

### Step 1 — Identify the target surface

Before touching anything, confirm:
- Which page or frame is the target?
- Is it canonical, draft, or governance?
- What is the intended final state (repaired existing design vs. net-new design)?
- Does the current agent have live Figma write access for this run?

Use `use_figma` to list pages and top-level frames:

```js
const pages = figma.root.children.map(p => ({
  name: p.name, id: p.id, childCount: p.children.length
}));
return pages;
```

### Step 2 — Audit the current surface

Inspect what exists. Do not assume — read it.

For each major region:
- Are fills bound to DS variables or hardcoded?
- Are components canonical library instances or locally duplicated frames?
- Are spacing and radius values token-backed?
- Are text nodes using DS-defined type styles?

Use inspection scripts from `ds-governance.md` as needed.

### Step 3 — Discover available DS assets

Before building anything new, inventory what the DS already provides:

```js
// List local variable collections
const collections = await figma.variables.getLocalVariableCollectionsAsync();
return collections.map(c => ({
  name: c.name, id: c.id,
  modes: c.modes.map(m => m.name),
  varCount: c.variableIds.length
}));
```

```js
// List existing components across all pages
const results = [];
for (const page of figma.root.children) {
  await figma.setCurrentPageAsync(page);
  page.findAll(n => {
    if (n.type === 'COMPONENT' || n.type === 'COMPONENT_SET')
      results.push({ page: page.name, name: n.name, type: n.type, id: n.id, key: n.key });
    return false;
  });
}
return results;
```

Match what exists before composing anything new.

### Step 4 — Apply the Incomplete DS Execution Protocol

For each major region and component in the design, follow the 5-tier fallback (see SKILL.md). Record which tier was used for each region. This becomes the DS depth report in the delivery report.

### Step 5 — Apply or generate the design

**For repair work:**
- Rebind fills to DS variables using `setBoundVariableForPaint`
- Rebind spacing, radius, and dimension properties using `setBoundVariable`
- Replace non-canonical frames with canonical component instances where applicable
- Repair naming and hierarchy to match the DS model

**For new generation:**
- Create a wrapper frame first, then build sections inside it (never top-level)
- Import canonical components by key before building any section that could use them
- Bind all colors, spacing, and radii to DS variables from the start
- Use `layoutSizingHorizontal/Vertical = 'FILL'` only after `parent.appendChild(child)`

Do not continue past this step if the agent cannot write to Figma. Re-route instead of faking a design deliverable in another surface.

### Step 6 — Validate

After every section or meaningful edit:
1. `get_metadata` — confirm node structure, parent-child hierarchy, component instance presence
2. `get_screenshot` — confirm visual result is not clipped, spacing is legible, mode is correct
3. Spot-check critical node data — variable bindings on fills, text content, component properties

If screenshot and node data disagree, report the mismatch. Do not silently pick one.

---

## Token Binding Patterns

### Color fill via variable
```js
const variable = await figma.variables.getVariableByIdAsync("VariableID:xxx:yyy");
const paint = figma.variables.setBoundVariableForPaint(
  { type: 'SOLID', color: { r: 0, g: 0, b: 0 } },
  'color',
  variable
);
node.fills = [paint];
```

### Spacing / radius via variable
```js
const variable = await figma.variables.getVariableByIdAsync("VariableID:xxx:yyy");
node.setBoundVariable('paddingLeft', variable);
node.setBoundVariable('paddingRight', variable);
node.setBoundVariable('cornerRadius', variable);
```

### Import component by key
```js
const componentSet = await figma.importComponentSetByKeyAsync("component-key-here");
const variant = componentSet.defaultVariant;
const instance = variant.createInstance();
parentFrame.appendChild(instance);
instance.layoutSizingHorizontal = 'FILL'; // AFTER appendChild
```

---

## Output Artifacts

- Repaired or newly generated Figma design
- DS-connected variable bindings, component instances, and text styles
- Direct screen or page link for review
- Skill-Wide Delivery Report (see `delivery-report.md`)

---

## Stop and Ask When

- The target Figma page is unclear or has an ambiguous role
- The design surface is too ambiguous to know what to preserve vs. replace
- The user has not confirmed whether output should stay in Figma or become a demo
- The DS is missing a canonical pattern required for the requested design
- The current agent cannot write to the target Figma file

---

## Confidence Signals

High when:
- Target Figma surface is explicit
- Canonical DS components exist for the required patterns
- Bindings and page ownership are clear
- Task is repair or bounded extension, not invention
- Live Figma write and validation are both available

Low when:
- The design intent is underspecified
- DS components for the needed patterns don't exist
- The task would require creating new DS semantics
- The agent cannot validate the written Figma result with metadata and screenshot
