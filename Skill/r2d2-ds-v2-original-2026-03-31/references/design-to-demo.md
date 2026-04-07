# Design To Demo — Full Workflow

Use this scenario when the user has an existing Figma design and wants a non-production demo, prototype, or sample implementation generated from it.

## Child Skills for This Scenario

| Skill | Role | Required? |
|-------|------|-----------|
| `figma-use` | Figma reads, component inspection, prototype reactions | Required |
| `audit-design-system` | Inspect source surface — identifies what is canonical vs. approximate | Required |
| `apply-design-system` | Bounded DS repair on source before demo generation | Optional |
| `rad-spacing` | Spacing cleanup on generated demo | Optional |
| `clarify` | Label and copy clarification | Optional |
| `normalize` | Convention cleanup | Optional |

If `figma-use` or `audit-design-system` are not installed, stop and tell the user to install them. For optional skills, fall back to the inline workflow below and note the limitation in the delivery report.

The Figma design is the primary source of truth. The goal is correct look and feel, actual DS usage, and usable demo behavior — not production-grade implementation quality.

Do not route here when:
- The main task is still editing the Figma design itself (→ DS To Design)
- The user expects production-grade code, stable code mapping, or handoff quality (→ DS To Code)

---

## Required Inputs

- Figma canonical surface (URL or node ID)
- Canonical source token JSON
- Supporting governance docs when available

---

## Execution Order

A step may be skipped only if explicitly not applicable — state why before skipping.

### Step 1 — Inspect the source token JSON

Before reading the Figma surface, understand the active semantic layer from the token JSON:
- What are the semantic color roles? (background/general, text/primary, fill/action, etc.)
- What spacing scale is in use?
- What are the component-level tokens if any?

This gives a reference baseline to compare against what Figma actually uses.

### Step 2 — Inspect and audit the source Figma surface

Use `use_figma` to read the source design:
- What pages and frames exist?
- Which regions use canonical component instances vs. locally assembled frames?
- Are fills and spacing bound to DS variables?
- What text styles and effect styles are applied?

```js
// Inspect component instances on the source frame
const frame = await figma.getNodeByIdAsync("source-frame-id");
const instances = frame.findAll(n => n.type === "INSTANCE");
return instances.map(i => ({
  id: i.id, name: i.name,
  mainComponent: i.mainComponent?.name,
  isLibraryComponent: i.mainComponent?.remote
}));
```

Identify what is canonical versus approximate. This determines which demo sections can claim DS depth and which are approximations.

### Step 3 — Apply bounded DS repair if needed

If the source design has significant binding drift that would produce an inaccurate demo, perform the minimal repair before demo generation:
- Rebind fills to DS variables
- Fix critical naming issues
- Do not perform broad page-level rewrites in this step — keep it contained

### Step 4 — Determine demo output format

Confirm with the user if not already clear:
- In-Figma prototype with reactions (navigate between screens)
- HTML/CSS demo page
- Code component demo
- Interactive prototype in another tool

Adjust the generation approach based on the format.

### Step 5 — Generate the demo

Apply the Incomplete DS Execution Protocol (see SKILL.md) for every major region and component in the demo output. For each region, use the deepest DS tier available and record the tier used.

**For Figma prototype output:**
- Build prototype reactions using `node.reactions` with the `actions` array format:
```js
node.reactions = [{
  actions: [{
    type: "NODE",
    destinationId: destFrame.id,
    navigation: "NAVIGATE",
    transition: {
      type: "MOVE_IN",
      direction: "LEFT",
      matchLayers: false,
      duration: 0.3,
      easing: { type: "EASE_OUT" }
    },
    preserveScrollPosition: false
  }],
  trigger: { type: "ON_CLICK" }
}];
```

**For code demo output:**
- Structure and naming should reflect DS semantics, not only visual appearance
- Map token names from source token JSON to CSS variables or equivalent
- Do not hardcode hex values when a semantic token maps the same intent

### Step 6 — Validate

1. `get_metadata` — confirm structure, component instances present, hierarchy correct
2. `get_screenshot` per section — check for clipped text, overlapping elements, wrong mode
3. Spot-check critical UI text and component state in node data (do not rely on screenshot alone)

---

## Output Artifacts

- AI demo, interactive prototype, or sample implementation
- Note stating whether the demo is: component-driven / locally componentized / mostly approximate
- Review links to the source Figma surface when helpful for fidelity context
- Skill-Wide Delivery Report (see `delivery-report.md`)

---

## Stop and Ask When

- The wrong Figma source may have been selected
- The user has not confirmed whether they want a demo or a Figma design
- The source design is too incomplete to determine what behavior or states the demo should include
- The DS does not expose enough reusable patterns and the missing scope would force broad invention

---

## Confidence Signals

High when:
- Source Figma surface is explicit and stable
- Source token JSON is explicit and usable
- Major patterns can be built from existing DS components or small local reusable components
- Screenshot and node-data validation agree on critical UI states

Low when:
- Source design is incomplete or loosely assembled
- DS is missing the patterns needed for the requested behavior
- Output scope is unclear between demo and production
