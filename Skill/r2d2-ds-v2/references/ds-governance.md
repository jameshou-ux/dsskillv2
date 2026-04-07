# DS Governance — Full Workflow

Use this scenario when the goal is to keep the DS complete, readable, stable, and governable.

## Child Skills for This Scenario

| Skill | Role | Required? |
|-------|------|-----------|
| `figma-use` | Figma reads, writes, binding repair | Required |
| `audit-design-system` | Drift identification and audit reports | Required |
| `figma-generate-library` | Phase decisions and work order | Required |
| `sync-figma-token` | Token parity verification | Optional |
| `rad-spacing` | Spacing/hierarchy cleanup | Optional |
| `clarify` | Copy and label fixes | Optional |
| `normalize` | Convention unification | Optional |

If `figma-use`, `audit-design-system`, or `figma-generate-library` are not installed, stop and tell the user to install the missing skill before proceeding. Do not substitute the inline inspection scripts below as a replacement for the full skill capability.

Governance tasks:
- Figma DS integrity and page canonization
- Token parity and adapter-driven updates
- Spacing, naming, and structure cleanup
- Canonical page hardening
- Identifying drift and reconnecting the DS to its formal record

---

## Required Input

The canonical SSOT source token JSON must be present before meaningful governance work begins.

If missing: stop and tell the user it is required. Governance decisions need a formal semantic record, not only the current Figma state.

---

## Execution Order

1. **Identify the target surface.** Confirm whether the page is canonical, reference, or governance before any edits.
2. **Inspect current state.** Use the Figma MCP (`use_figma`) to read node structure, variable bindings, component usage, and naming.
3. **Audit drift.** Compare Figma state against the canonical source token JSON:
   - Are variable bindings present or are hex/literal values hardcoded?
   - Are component names and variant axes consistent with the token model?
   - Are spacing, radius, and type values traceable to token definitions?
   - Are page roles and section boundaries clearly labeled?
4. **Classify the change.** Decide whether the fix belongs in:
   - Figma (binding repair, naming fix, structural cleanup)
   - SSOT token JSON (semantic gap or incorrect definition)
   - Adapter JSON (transformation mismatch)
   - Docs (governance record or annotation)
5. **Apply the smallest correct change.** Work in bounded, contained edits. Do not rewrite whole pages in one pass.
6. **Re-audit.** Confirm the drift is resolved. Do not assume — verify.
7. **Sync records.** If semantics changed, update the relevant governance doc, adapter JSON, or token annotation to reflect the new canonical state.

---

## Audit Checklist

For each Figma surface under audit, confirm:

- [ ] All color fills are bound to DS variables, not hardcoded hex values
- [ ] All spacing, radius, and dimension values are bound to DS tokens or match token-defined values
- [ ] Typography uses DS-defined font family, weight, size, line height, and letter spacing
- [ ] Component instances reference canonical library components, not locally duplicated frames
- [ ] Component naming and variant axes match the canonical DS model
- [ ] Page and section labels correctly identify the role (canonical, governance, reference, draft)
- [ ] Governance records exist for any non-canonical pattern currently in use

---

## Figma Inspection Pattern

Use `use_figma` to inspect variable bindings and component usage on the target surface:

```js
// List all variable bindings on a frame
const frame = figma.currentPage.findOne(n => n.name === "Target Frame");
const bindings = [];
frame.findAll(() => true).forEach(node => {
  const bv = node.boundVariables;
  if (bv && Object.keys(bv).length > 0) {
    bindings.push({ id: node.id, name: node.name, type: node.type, bindings: Object.keys(bv) });
  }
});
return bindings;
```

```js
// Detect hardcoded fills (no variable binding)
const frame = figma.currentPage.findOne(n => n.name === "Target Frame");
const unbound = [];
frame.findAll(() => true).forEach(node => {
  if ('fills' in node && node.fills && node.fills.length > 0) {
    node.fills.forEach(fill => {
      if (fill.type === 'SOLID' && !fill.boundVariables?.color) {
        unbound.push({ id: node.id, name: node.name, fill: fill.color });
      }
    });
  }
});
return unbound;
```

---

## Output Artifacts

- Repaired Figma governance or canonical pages
- Corrected variable, style, or component bindings
- Token parity or drift notes
- Explicit record of what changed and why

---

## Stop and Ask When

- The SSOT token source is missing or disputed
- The page role is unclear between governance, canonical, and reference
- A change may alter accepted semantics rather than only fix drift
- The task could be governance work or application work and user intent is not explicit

---

## Confidence Signals

High when:
- Canonical source token JSON exists and is unambiguous
- Page role is clear
- Drift is concrete and local
- Fix is parity-preserving, not semantic invention

Low when:
- SSOT is disputed or outdated
- Multiple token sources exist with conflicting values
- The "fix" would require redefining DS semantics
