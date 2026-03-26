# Figma DS Cleanup Plan

Date: 2026-03-25

Target Figma file:
`https://www.figma.com/design/DBQdb8ymhIfTPS9GmcTqaR/-%E6%B5%8B%E8%AF%95--webapp-DS?node-id=321-9714`

Target node:
`321:9714` (`📦 设计组件和定义`)

## Goal

Clean up and normalize the existing Figma design-system file without corrupting current assets, while aligning it to the repository token pipeline and establishing a safe migration path for components and screens.

This is a governance and migration task, not a clean-room generation task.

## What We Observed

### Repo side

- The repo already has a token adaptation pipeline:
  - `source/tokens.json`
  - `adapters/figma/figma_tokens_v2.json`
  - `tools/build-figma-adapter.py`
  - `figma-plugin/`
- The README defines the intended flow:
  - `canonical tokens -> normalize (optional) -> adapt -> figma adapter payload -> Figma plugin import`
- The current source and adapter are not identical:
  - `source/tokens.json` currently counts:
    - `Primitive`: 64
    - `Light`: 86
    - `Dark`: 86
  - `adapters/figma/figma_tokens_v2.json` currently counts:
    - `primitive`: 93
    - `semantic/light`: 47
    - `semantic/dark`: 47
    - `pattern/*`: 0
    - `component/*`: 0
- The plugin README explicitly says the `v2` adapter intentionally excludes `pattern` and `component` layers from Figma import.

### Figma side

- The Figma file already contains local variables, text styles, effect styles, and components.
- Current local variable collections:
  - `Primitive` with modes `Light`, `Dark`
  - `Semantic` with modes `Light`, `Dark`
  - `Pattern` with modes `Light`, `Dark`
  - `Component` with modes `Light`, `Dark`
- Current counts visible through inventory:
  - 4 local collections
  - 173 local variables
  - 10 text styles
  - 4 effect styles
  - 59 components
  - 16 component sets
- The main page `📦 设计组件和定义` is a board-style showcase page, not a clean library page.
- Existing component names and variant axes are inconsistent and partly generic:
  - `Property 1=Default`
  - `Property 1=Expand`
  - `Status=Unsigned in`
  - `Type=Double horitontal`
  - `Hiearachy=L2`
- Several placeholder library pages already exist but are empty:
  - `原子组件/Navigation`
  - `原子组件/Button`
  - `原子组件/Modal`
  - `原子组件/Toast+Dialog`
  - `原子组件/Toggle`
  - `原子组件/Backdrop`
  - `业务组件/Error`

## Key Conclusion

Do not start with `cc-figma-tokens` or `cc-figma-component`.

Why:

- Those skills assume a cleaner target schema than the current file has.
- The file already uses a custom 4-collection, 2-mode variable model.
- The repo's current Figma adapter intentionally excludes `pattern` and `component` from import, while the Figma file already contains `Pattern` and `Component` collections.
- Running contract-generation skills immediately would likely harden drift instead of reducing it.

The correct first move is:

1. inventory
2. dry-run token drift analysis
3. structural DS audit
4. decide repair vs partial rebuild

## Recommended Skills By Phase

### Phase 0: Discovery and drift reporting

Use:

- `figma-use`
- `figma-generate-library`
- `sync-figma-token`
- `audit-design-system`

Purpose:

- read current Figma state
- compare Figma variables with source token structure
- identify which components are structurally repairable
- decide what should be preserved, migrated, or rebuilt

### Phase 1: Foundation normalization

Use:

- `figma-use`
- `figma-generate-library`
- `sync-figma-token`

Purpose:

- normalize collections, naming, scopes, code syntax, and style structure
- decide whether the existing `Pattern` and `Component` collections remain in Figma or get phased out from the variable layer

### Phase 2: Component cleanup and migration

Use:

- `figma-use`
- `audit-design-system`
- `apply-design-system`
- `rad-spacing`

Purpose:

- clean naming
- convert bad wrappers / detached frames into proper instances or canonical local component sets
- fix auto-layout and spacing hierarchy
- migrate component examples from the showcase board into the dedicated component pages

### Phase 3: Code governance

Use:

- `sync-figma-token`
- `figma-code-connect-components`

Purpose:

- keep token parity stable
- connect mature published components back to code

## Practical Execution Plan

### Step 1: Produce three baseline reports

No writes yet.

#### 1A. Figma inventory report

Read-only `use_figma` script should output:

- collections, modes, variable counts
- variables missing scopes or using questionable naming
- text styles and effect styles
- component sets and variant counts
- components that are not in component sets
- components with inconsistent variant axes
- likely non-auto-layout components
- components whose internal layers use placeholder names

#### 1B. Token drift report

Run `sync-figma-token` as dry-run only.

Policies:

- `direction`: `code_to_figma`
- `deletePolicy`: `archive_only`
- `conflictPolicy`: `manual_review`
- `namingPolicy`: dot-path source to slash-path Figma normalization
- `modePolicy`: map source `Light/Dark` to Figma `Light/Dark`

This step must stop after dry-run output.

#### 1C. High-value component audit report

Run `audit-design-system` on a focused set of nodes first:

- `Button`
- `Nav` / `Web nav` / `Mobile nav`
- `Modal`
- `Toast`
- `Breadcrumb`
- `Toggle`

Do not audit the whole board at once.

## Repair vs Rebuild Decision

After Step 1, use this decision rule.

### Choose repair-in-place if

- current collections are structurally understandable
- most variable names can be canonically mapped
- semantic alias chains are recoverable
- components are messy but not conceptually duplicated beyond repair

### Choose partial rebuild if

- variable taxonomy is inconsistent at the collection boundary
- scopes and code syntax are broadly wrong
- `Pattern` and `Component` variable layers are not serving a clear Figma consumption purpose
- component examples and canonical component sources are mixed together on the same board

For this file, partial rebuild is the more likely outcome.

Specifically:

- keep the current file as the migration target
- do not delete the board page
- rebuild normalized foundations on dedicated pages
- migrate one component family at a time
- leave the existing showcase board as evidence and regression reference

## Recommended Automation Strategy

### Automation lane A: local token preparation

Use local repo scripts first.

Potential script path:

- `tools/build-figma-adapter.py`

Suggested output artifacts:

- `/tmp/figma-adapter-next.json`
- `/tmp/figma-token-drift-report.json`

Purpose:

- normalize source tokens into the adapter contract
- compare normalized output with current Figma collection model before any write

### Automation lane B: Figma inventory scripts

Use `figma-use` with small read-only scripts.

Suggested script outputs:

- `/tmp/figma-ds-inventory.json`
- `/tmp/figma-component-audit.json`
- `/tmp/figma-style-inventory.json`

Purpose:

- create a stable baseline
- support repeatable comparison before and after cleanup

### Automation lane C: controlled cleanup writes

Only after approval.

Write scripts should be split by concern:

1. foundations cleanup
2. style cleanup
3. one component family per run
4. board-to-library migration

Never perform all cleanup in one `use_figma` call.

## First Write Scope

When writes begin, the safest first write scope is not variables.

Start with structure:

1. create or normalize dedicated library pages
2. duplicate one component family from the board into its target page
3. clean naming and auto-layout for that family
4. validate with screenshot

Best first family:

- `Button`

Why:

- it has many visible variants
- it reveals variant-axis problems immediately
- it is easy to validate visually

## What Not To Do

- Do not bulk overwrite all variables in the existing file on the first pass.
- Do not run `cc-figma-tokens` against this file as-is.
- Do not assume `Pattern` and `Component` collections should survive unchanged.
- Do not rename or restructure the entire board in one operation.
- Do not parallelize any `use_figma` write calls.

## Immediate Next Step

If continuing automation, the next concrete action should be:

1. generate a machine-readable inventory from the Figma file
2. generate a dry-run token drift report from local source -> target Figma schema
3. classify the file into:
   - preserve
   - normalize
   - rebuild

Then approve the first write scope before any mutation.
