# DS To Code — Full Workflow

Use this scenario when the output requires production-facing implementation quality, stable code mapping, or handoff-grade code output.

## Child Skills for This Scenario

| Skill | Role | Required? |
|-------|------|-----------|
| `figma-use` | Figma surface inspection, bounded hardening | Required |
| `audit-design-system` | Canonical readiness verification | Required |
| `figma-implement-design` | Node-to-code translation | Required |
| `figma-code-connect-components` | Durable component-to-code mapping | Optional |

If `figma-use`, `audit-design-system`, or `figma-implement-design` are not installed, stop and tell the user to install the missing skill before proceeding. DS To Code without these skills cannot meet production-facing quality.

This is a higher bar than demo scenarios. Do not route here unless the target surface is canonical and the component family is stable.

---

## Readiness Gate

Before any code generation, verify all of the following. If any condition is not met, stop at DS Governance or DS To Design first.

- [ ] The target Figma surface is canonical (not a draft, governance page, or historical cleanup surface)
- [ ] Component naming and variant axes are stable and would not require renaming during mapping
- [ ] Token semantics are stable enough to map to code-side usage without ambiguity
- [ ] The intended handoff surface can be validated without relying on governance history
- [ ] The user has confirmed that production-facing quality — not demo quality — is the requirement

---

## Required Inputs

- Canonical Figma surface (confirmed canonical, not draft or governance)
- Canonical source token JSON
- Target codebase or framework context (what stack? what component library?)
- Confirmation that the component family is stable enough for durable mapping

---

## Execution Order

A step may be skipped only if explicitly not applicable — state why before skipping.

### Step 1 — Verify canonical readiness

Inspect the Figma surface to confirm it meets the readiness gate:

```js
// Check component instances on the target surface
const frame = await figma.getNodeByIdAsync("canonical-frame-id");
const instances = frame.findAll(n => n.type === "INSTANCE");
const nonLibrary = instances.filter(i => !i.mainComponent?.remote);
return {
  totalInstances: instances.length,
  libraryInstances: instances.length - nonLibrary.length,
  localInstances: nonLibrary.map(i => ({ id: i.id, name: i.name }))
};
```

If significant local (non-library) instances exist, the surface may not be stable enough for code mapping without first applying DS To Design.

### Step 2 — Harden the Figma surface if needed

If the surface is close but not yet ready:
- Rebind unbound fills and spacing to DS variables
- Replace local approximations with canonical library component instances where applicable
- Fix naming inconsistencies that would create confusing code mappings

Keep changes bounded and targeted. Validate with `get_metadata` and `get_screenshot` after each change.

### Step 3 — Extract the design specification

Read the design surface systematically:
- Component hierarchy and instance structure
- Variant properties and their values
- Typography: family, weight, size, line height, letter spacing
- Color tokens mapped to their semantic paths
- Spacing, radius, and sizing values mapped to their token paths
- Interaction states if applicable

Map each design value to its source token JSON path. This becomes the handoff specification.

### Step 4 — Generate the code output

Apply the Incomplete DS Execution Protocol for every component and region. For each:
- Use the DS token path as the reference, not the resolved hex value
- Map to the target codebase's token system if one exists
- Use the target framework's component model if a mapped component exists
- Document any case where a DS component does not have a code equivalent

**Token mapping pattern:**
```
DS token path:  semantic/background/card → gray.900 → #1C1C1E
Code-side:      var(--color-background-card) or theme.colors.backgroundCard
```

**Do not:**
- Hardcode resolved hex values when a semantic token maps the same intent
- Create new component abstractions without documenting the DS source
- Skip variant mapping — each code component prop should trace to a Figma variant axis

### Step 5 — Validate the handoff

- Confirm the generated code references match the Figma surface structure
- Verify token mappings are one-to-one with the source token JSON
- If Code Connect mappings are involved, confirm the component key is stable

---

## Output Artifacts

- Production-facing implementation or handoff-ready code output
- Explicit statement of the source Figma surface used for handoff
- Token mapping table (DS path → code-side reference)
- Mapping or fidelity notes when component families are involved
- Confidence and residual risk report for implementation readiness
- Skill-Wide Delivery Report (see `delivery-report.md`)

---

## Stop and Ask When

- The target handoff surface is not confirmed canonical
- The user has not clarified whether demo quality or production quality is the bar
- The component family is unstable enough that code mapping would be misleading or short-lived
- Figma handoff constraints conflict with codebase constraints and the tradeoff is not explicit

---

## Confidence Signals

High when:
- Source surface is canonical and stable
- Variant axes and naming are explicit and stable
- Token semantics are mappable to code-side usage without ambiguity
- Output bar is production-facing and agreed by the user

Low when:
- Component naming is inconsistent or in flux
- The Figma surface has significant non-library instances
- Token semantics are ambiguous between modes or collections
- The user has not confirmed production quality is required
