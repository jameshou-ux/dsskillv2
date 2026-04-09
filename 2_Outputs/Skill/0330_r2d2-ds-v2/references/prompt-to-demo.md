# Prompt To Demo — Full Workflow

Use this scenario when a prompt, PRD, or product intent is the primary source and the output is a demo or prototype.

## Child Skills for This Scenario

| Skill | Role | Required? |
|-------|------|-----------|
| `figma-use` | Live Figma reads, writes, variable binding, prototype reactions | Conditional |
| `figma-generate-design` | DS-backed screen and section generation from intent | Optional (strongly recommended) |
| `edit-figma-design` | Text-driven design iteration | Optional |
| `audit-design-system` | Post-generation validation | Optional |
| `apply-design-system` | DS reconnection if generated surface drifts | Optional |

`figma-use` is required when the output is written to Figma or when live DS asset discovery is needed from the canonical file. For code or HTML demo output, the scenario may proceed without live Figma access only if the token JSON exists and the evidence basis is clearly limited.

If `figma-generate-design` is not installed, note the limitation and use the inline generation workflow below instead. Do not claim `canonical-component` depth unless canonical component evidence is actually available.

This is the most DS-discipline-intensive scenario: without an existing Figma surface to reference, the agent must derive the full visual and structural decisions from the DS alone.

**Important re-route rule:** If the user says "demo" or "prototype" but actually wants the final artifact written to Figma as a design, re-route to DS To Design before execution.

---

## Required Inputs

- Canonical source token JSON (required, not optional)
- User intent source: prompt, PRD, product note, or design brief
- Relevant Figma file with DS components and variables, or a supplied design-context bundle for the exact DS surface

Live Figma access is required if:
- the final output will be written to Figma
- the run needs canonical component discovery from the live library

If only token JSON and screenshots are available, the run may still produce a demo, but DS depth is capped by the evidence actually present.

---

## Execution Order

A step may be skipped only if explicitly not applicable — state why before skipping.

### Step 1 — Parse the intent source

Before touching Figma or writing any output:
- What screens or sections are needed?
- What user flows are involved?
- What states must the demo cover (empty, loading, success, error, etc.)?
- What DS components are likely involved for each section?

If the intent is too vague to answer these questions confidently, stop and ask before proceeding. Do not guess scope.

### Step 2 — Inspect the canonical source token JSON

Extract the active semantic layer:
- Semantic color roles (background/*, text/*, fill/*, border/*, status/*)
- Spacing scale and sizing tokens
- Component-level tokens if defined
- Primitive palette as fallback reference

This is the constraint set for all visual decisions in the demo.

### Step 3 — Inventory available DS assets in Figma or supplied design context

Before building anything, check what the DS already provides. This determines which regions can use Tier 1 (canonical component) vs. lower tiers.

```js
// List all components and component sets across all pages
const results = [];
for (const page of figma.root.children) {
  await figma.setCurrentPageAsync(page);
  page.findAll(n => {
    if (n.type === 'COMPONENT' || n.type === 'COMPONENT_SET')
      results.push({
        page: page.name, name: n.name,
        type: n.type, key: n.key, id: n.id
      });
    return false;
  });
}
return results;
```

```js
// List variable collections and their variables
const collections = await figma.variables.getLocalVariableCollectionsAsync();
const result = [];
for (const col of collections) {
  const vars = await Promise.all(col.variableIds.map(id => figma.variables.getVariableByIdAsync(id)));
  result.push({
    collection: col.name,
    modes: col.modes.map(m => m.name),
    variables: vars.map(v => ({ name: v.name, id: v.id, type: v.resolvedType }))
  });
}
return result;
```

If live Figma read is unavailable:
- use the exact supplied screenshots, metadata, governance docs, and token JSON as the evidence set
- do not invent component names, variant axes, or canonical patterns
- cap the highest claimable DS depth at `local-component` unless canonical component evidence is explicit in the supplied material

Map intent sections to DS assets. For each section, note which tier of the Incomplete DS Execution Protocol applies and what evidence supports that tier.

### Step 4 — Plan the composition before building

Before any `use_figma` write:
- List each screen or section
- For each, state the DS tier being used (component / pattern / semantic / primitive / gap)
- For each, state the evidence basis (live Figma / design-context bundle / screenshot only / token JSON only)
- Identify which sections will require Tier 5 approximations and flag them

This is the DS depth plan. Share it with the user briefly if Tier 5 approximations are significant.

### Step 5 — Build the output

**For Figma output (when user wants prototype in Figma):**

Create the page wrapper frame first, then build each section inside it — never reparent later:

```js
// Find clear space on page
let maxX = 0;
for (const child of figma.currentPage.children) {
  maxX = Math.max(maxX, child.x + child.width);
}
const wrapper = figma.createFrame();
wrapper.name = "Screen Name";
wrapper.layoutMode = "VERTICAL";
wrapper.resize(390, 100); // mobile width
wrapper.layoutSizingVertical = "HUG";
wrapper.x = maxX + 200;
wrapper.y = 0;
return { wrapperId: wrapper.id };
```

Build one section per `use_figma` call. Validate with `get_screenshot` after each section before proceeding.

**For code/HTML demo output:**
- Structure naming and grouping should reflect DS semantic roles, not visual shape
- Map token paths from source token JSON to output variables
- Do not hardcode hex values when a semantic token covers the intent
- Do not present local markup as a canonical DS component unless the canonical source was actually verified

**Generation discipline:**
- Never start from a clone-based page as the final method unless the user explicitly asks
- Prefer component-driven build order over frame-driven build order
- If a business block appears more than twice, make it the smallest reusable local component first
- Separate what is truly componentized from what is only token/style-aligned
- If live Figma evidence is missing, be stricter, not looser. Lower the confidence and depth claim instead of filling gaps with invented DS structure.

### Step 6 — Add prototype reactions (if Figma output)

Wire navigate reactions between screens after all screens are built:

```js
// Get all screen frames
const screens = [
  await figma.getNodeByIdAsync("screen1-id"),
  await figma.getNodeByIdAsync("screen2-id"),
];

// Wire CTA button on screen 1 to navigate to screen 2
const ctaButton = screens[0].findOne(n => n.name === "CTA Button");
ctaButton.reactions = [{
  actions: [{
    type: "NODE",
    destinationId: screens[1].id,
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
return { success: true };
```

### Step 7 — Validate

1. `get_metadata` — structure, component instances, hierarchy
2. `get_screenshot` per screen — no clipped text, no overlapping, correct mode, correct spacing
3. Node data spot-check — CTA text, key labels, variable bindings on critical fills

---

## DS Depth Reporting

The delivery report must explicitly state for each major section:

- `canonical-component` — DS library component instance used
- `local-component` — smallest reusable local component built from DS tokens
- `semantic-token` — composed from semantic tokens, no component
- `primitive-token` — composed from primitives, no semantic token
- `visual-approximation` — Tier 5 gap; report what was approximated and why

Do not report "uses the DS" without specifying the depth.

---

## Output Artifacts

- AI demo or prototype driven by prompt and DS constraints
- Explicit note on DS surfaces, components, and token layers used per section
- Skill-Wide Delivery Report (see `delivery-report.md`)

---

## Stop and Ask When

- The prompt is too vague to determine screen scope, states, or output shape
- The user has not confirmed whether the output should be a demo or a Figma design
- The prompt requires a business pattern not in the DS that would need semantic invention
- The DS surfaces are too weak to choose a stable composition
- The user expects canonical component fidelity but no live Figma or explicit design-context evidence is available

---

## Confidence Signals

High when:
- Prompt clearly defines the page or flow scope
- Source token JSON is available and usable as a semantic constraint
- DS already has canonical surfaces that match the requested interaction pattern
- Output surface is clearly demo-oriented
- Chosen composition can be explained without inventing new DS rules

Low when:
- Intent is underspecified (missing states, unclear scope)
- DS lacks patterns for the requested flow
- The composition would require significant Tier 5 approximation
- Only token JSON or screenshots are available and canonical component evidence cannot be verified
