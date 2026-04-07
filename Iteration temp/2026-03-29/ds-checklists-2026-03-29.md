# DS Checklists

Date: 2026-03-29

## 1. Source Token Optimization Checklist

Goal:

- determine whether the current token source can serve as a stable SSOT

### Single Source

- [ ] one canonical token source is explicitly designated
- [ ] all other token JSON files are marked as snapshot, adapter output, or derived output
- [ ] both humans and AI can tell which file is the formal edit surface

### Naming

- [ ] top-level layer naming is fully consistent
- [ ] token path naming style is fully consistent
- [ ] alpha and opacity naming rules are consistent
- [ ] typography token naming is consistent across role, style, and scale

### Layer Boundaries

- [ ] `primitive` contains raw values only
- [ ] `semantic` contains cross-component semantic values only
- [ ] `pattern` contains cross-component composition semantics only
- [ ] `component` contains family-local alias or recipe semantics only
- [ ] no token obviously belongs in `semantic` but is stored in `component`
- [ ] no token obviously belongs in `component` but is over-promoted to `pattern`

### Token Quality

- [ ] high-frequency tokens have clear `$description`
- [ ] alias path rules are consistent
- [ ] light and dark mode structure is consistent
- [ ] typography structure is complete and stable
- [ ] spacing, radius, and size tokens do not have avoidable duplication
- [ ] effect, shadow, and blur rules are explicit rather than ad hoc

### Governance Metadata

- [ ] there is a document that explains the four token layers and their intended use
- [ ] there is a document that explains which token categories are expected to bind directly in Figma
- [ ] there is a document that explains how newly discovered tokens are written back to source
- [ ] deprecated or transitional tokens can be identified clearly

### Operational Readiness

- [ ] Figma-discovered missing tokens can be written back into the active token source cleanly
- [ ] source token changes can produce stable downstream adapter outputs
- [ ] AI can read the token source without confusion from duplicated files

### Working Assessment

- [ ] current source token structure is stable enough to be treated as the active SSOT
- [ ] current source token structure still needs targeted optimization before serving as strong SSOT

## 2. Figma AI-to-Code Readiness Checklist

Goal:

- determine whether the current Figma DS is ready to support stable AI to code workflows

### Canonical Surface

- [ ] canonical component pages are explicitly identified
- [ ] governance and history pages are explicitly identified
- [ ] downstream handoff defaults to canonical pages rather than cleanup boards
- [ ] mature component families include both definition and example areas

### Component API

- [ ] variant axis naming is readable
- [ ] boolean property naming is readable
- [ ] weak names such as `Property 1` or `Variant5` are removed from mature families
- [ ] public component APIs are stable enough to map downstream
- [ ] major component states are covered in the design surface

### Token Binding

- [ ] high-frequency colors are bound to semantic tokens
- [ ] spacing, radius, and size usage is mostly tokenized
- [ ] text styles are stable and used consistently
- [ ] effect styles follow an explicit system rather than raw local effects
- [ ] remaining unbound values are known exceptions rather than unknown residue

### Pattern Readiness

- [ ] common patterns are distinct from single components
- [ ] pattern naming expresses function, not only appearance
- [ ] AI can tell which compositions are reusable and which are only examples

### Design-to-Code Bridge

- [ ] at least one mature family is ready for code mapping
- [ ] Figma property names can map to code-side props
- [ ] token names can map to code-side token usage
- [ ] component structure is stable enough that AI does not need to infer basic semantics from screenshots alone
- [ ] a path exists for Code Connect or an equivalent mapping layer

### Behavior And Implementation Coverage

- [ ] interaction states are represented clearly enough for implementation
- [ ] responsive behavior is represented or documented clearly enough for implementation
- [ ] loading, empty, and error states are represented where relevant
- [ ] accessibility-critical behavior is not left entirely implicit
- [ ] generated code can be validated against stable canonical surfaces

### Pilot Readiness

- [ ] at least one simpler family is ready for AI to code pilot work
- [ ] at least one more complex family is ready for second-phase pilot work
- [ ] the operating model assumes pilot-first expansion rather than full-file code generation

### Working Assessment

- [ ] current Figma DS is ready for controlled AI to code pilots
- [ ] current Figma DS is ready for broad AI to code production workflows
- [ ] current Figma DS still needs canonical-page hardening before AI to code should expand

## Recommended Use

Use this file to:

- mark current readiness
- track gaps before expanding AI workflows
- separate token-source problems from Figma-surface problems
- decide whether the next move should be token cleanup, page canonization, prototype work, or code mapping
