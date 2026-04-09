# Figma DS Workflow, Timeline, and Token Schema

Date: 2026-03-26

Target Figma file:
`DBQdb8ymhIfTPS9GmcTqaR`

Related source token file:
`Iteration temp/source_token_v5.json`

## 1. Recommended Skill Workflow

This workflow is for the current state of the Figma DS file: an existing library that already has variables, styles, component sets, showcase pages, and page-local cleanup history.

### Core skill set

- `figma-use`
  - mandatory base layer for every `use_figma` read or write
  - use for all Figma Plugin API inspection, mutation, migration, and page restructuring
- `figma-generate-library`
  - use as the orchestration layer for design-system work
  - defines the correct phase order: discovery -> foundations -> file structure -> components -> QA
- `audit-design-system`
  - use for read-only audits of pages, sections, or component families
  - best for finding drift: local wrappers, missing bindings, repeated custom frames, raw values
- `apply-design-system`
  - use when an existing page or section should be brought back onto system primitives or reorganized around canonical components
  - do not use for a single tiny fix
- `sync-figma-token`
  - use for code token vs Figma variable parity
  - always dry-run first, then stop, then apply in a separate step
- `rad-spacing`
  - use when the main issue is layout hierarchy, auto-layout spacing, or padding/gap normalization

### What each skill is for in this repo

#### `figma-use`

Use this whenever the task requires:

- inspecting pages, component sets, variables, styles, or node trees
- writing new variables or styles
- renaming component properties and variants
- cloning or moving components to new pages
- binding variables to fills, strokes, effects, spacing, or radius

In practice, this is the execution engine.

#### `figma-generate-library`

Use this to keep the work ordered correctly:

- first inspect and lock scope
- then clean or extend foundations
- then organize file structure
- then harden component pages
- then run QA

In practice, this is the governance and sequencing layer.

#### `audit-design-system`

Use this before adjustment passes to answer:

- is this node a proper component instance or a local construction
- are there repeated custom structures that should be componentized
- are tokens and styles actually bound
- is there variant drift or page-local inconsistency

In practice, this is the diagnostics layer.

#### `apply-design-system`

Use this when the scope is already known and broad enough to justify a section-level rewrite or normalization pass.

Typical use cases:

- reconnect a page section to canonical library components
- rebuild a showcase area from formal component definitions
- convert a drifted page from mixed local frames into a system-backed structure

In practice, this is the page-level remediation layer.

#### `sync-figma-token`

Use this only for token parity.

Typical checks:

- token exists in code but not in Figma
- alias target differs
- value differs across modes
- scopes or code syntax are wrong

In practice, this is the token-governance layer.

#### `rad-spacing`

Use this when the page is structurally correct but hierarchy is visually muddy because gaps and padding are inconsistent.

In practice, this is the layout-normalization layer.

### Recommended operating flow

For this repo and this Figma file, the practical flow should be:

1. `figma-use` for read-only inventory
2. `audit-design-system` for design-system drift diagnosis
3. `sync-figma-token` dry-run when token parity is involved
4. `figma-use` for targeted writes
5. `apply-design-system` when the adjustment is section-sized rather than node-sized
6. `rad-spacing` when spacing hierarchy needs normalization
7. `figma-use` again for final precise fixes and validation

### Full skill coverage beyond the main flow

The March 24 and March 25 skill set is broader than the current DS-governance loop. The skills below should still be covered explicitly, but not all of them belong inside the default cleanup flow.

#### Skills that belong in adjacent DS workflows

- `cc-figma-tokens`
  - use when the goal is to build or regenerate the Figma variable collections from a cleaner code token source
  - best fit for a controlled token-library rebuild, not for page-local cleanup on an already messy file
- `cc-figma-component`
  - use after token collections are already stable in Figma
  - best fit when a component contract is mature enough that the component family should be generated or refreshed from contract structure
- `figma-create-design-system-rules`
  - use to generate project-specific DS rules and operating conventions
  - best fit when the repo needs an explicit governance document or `AGENTS.md` section
- `figma-code-connect-components`
  - already relevant for this DS, but it belongs downstream of component-page stabilization
  - use when component APIs and canonical pages are stable enough to map to code

#### Skills that are useful but not part of the default cleanup loop

- `figma-create-new-file`
  - use when a new DS sandbox, branch file, or scratch reconstruction file is needed
  - not needed for the current in-place governance work because the target file already exists
- `figma-generate-design`
  - use when a full screen or view needs to be generated in Figma from code or a product description
  - useful after the DS is stable enough to serve as a source of imported primitives and components
- `edit-figma-design`
  - use when design work is primarily text-driven and not a token/component governance task
  - useful for exploratory concept work or iterating a specific screen from written feedback
- `multi-agent`
  - use for coordination around parallel read tasks, planning, or code-side implementation workflows
  - do not use it for parallel `use_figma` writes; Figma mutation still needs to stay sequential

#### How these omitted skills fit into the bigger picture

The complete mental model should be:

1. `figma-create-design-system-rules`
   - define project rules
2. `cc-figma-tokens`
   - build or regenerate canonical Figma token collections when needed
3. `cc-figma-component`
   - build or refresh contract-driven components when needed
4. main governance loop
   - `figma-use`
   - `figma-generate-library`
   - `audit-design-system`
   - `apply-design-system`
   - `sync-figma-token`
   - `rad-spacing`
5. downstream production flows
   - `figma-code-connect-components`
   - `figma-generate-design`
   - `edit-figma-design`
   - `multi-agent`
   - `figma-create-new-file`

### Recommended plan template

Use this plan on any page or family in the file:

1. Inspect
   - page structure
   - component sets and instances
   - variables, styles, and existing conventions
2. Audit
   - token/style binding coverage
   - system drift
   - repeated local structures
3. Decide scope
   - token fix
   - page cleanup
   - family cleanup
   - spacing normalization
4. Apply incrementally
   - one page or one family at a time
   - one write step per `use_figma` call
5. Re-audit
   - verify no visual regressions
   - verify no obvious residual drift

## 2. Timeline Of The Last 24 Hours

This timeline summarizes the actual work completed inside the Figma file during the last 24 hours. It is organized by execution phase, not wall-clock timestamps, because the work happened as a sequence of guided cleanup passes.

### Phase 0: Foundations cleanup and token binding recovery

Scope:

- current local variable model
- core component page
- binding cleanup across major families

Actions completed:

- normalized local variable `scope`
- normalized local variable `WEB code syntax`
- created missing semantic token `Semantic/text/inverse`
- backfilled the same token into `Iteration temp/source_token_v5.json`
- rebound obvious legacy remote color bindings to the current local semantic layer
- cleaned the last residual non-canonical bindings in:
  - `Button`
  - `Button-Web`
  - `Modal`
  - `Nav`
  - `Web nav`
  - `Mobile nav`
  - `Menu`
  - `Token list`
  - `Toast`
  - `Toggle`
  - `Breadcrumb`
  - `Bkg`
- moved core typography usage back to local text styles

Result:

- audited residual nonlocal bindings across the main component families reached `0`

### Phase 0.5: Token schema enrichment

The following missing semantic tokens were generated because the existing DS surface needed them but the source token schema did not provide them:

- `Semantic/text/inverse`
- `Semantic/fill/action`
- `Semantic/fill/action_subtle`
- `Semantic/stroke/logo`
- `Semantic/stroke/icon_inverse`

These were created in Figma and also added to `Iteration temp/source_token_v5.json`.

### Phase 1: Component API cleanup

Scope:

- public component API readability
- variant axis naming
- boolean property naming
- typo cleanup

Actions completed:

- `Nav`
  - `Property 1` -> `Variant`
- `Token list`
  - `Property 1` -> `State`
- `Menu`
  - `Property 1` -> `Status`
- `Mobile nav`
  - variants converged to `Level=Top nav` and `Level=Secondary nav`
- `Breadcrumb`
  - `Hiearachy` -> `Hierarchy`
- `Button-Web`
  - boolean properties renamed to `Show blur` and `Show description`
- `Modal`
  - public property API redesigned around readable text and platform fields
  - stale unused text properties removed

Result:

- the current high-value component families became much more readable from the property panel
- no broad rebuild was required

### Phase 2: Style governance review

Scope:

- local text styles
- local paint styles
- local effect styles

Findings:

- local text styles were already in a good canonical set and aligned with the semantic font model
- local gradients were sufficiently structured
- `component/button/primary/fill` and `component/button/primary/stroke` were intentionally retained as component-specific paint styles
- the global shadow scale was structurally clean

Result:

- Phase 2 started as an audit, not a destructive rewrite

### Phase 3: Page `3285:437` effect-style governance

Target page:

- `3285:437` / `组件Phase 1: Component Schema Cleanup`

Actions completed:

- retained `component/button/primary/fill`
- retained `component/button/primary/stroke`
- introduced and applied a unified `effect/...` naming namespace
- created page-local blur and shadow effect styles where repeated effect recipes existed

Final effect-state on the page:

- `59` effect-bearing nodes
- `59` styled nodes
- `0` bare effects

Final effect namespace on the page:

- `effect/blur/background-none`
- `effect/blur/background-md`
- `effect/blur/layer-xs`
- `effect/blur/layer-sm`
- `effect/blur/layer-md`
- `effect/blur/layer-lg`
- `effect/shadow/sm`
- `effect/shadow/md`
- `effect/shadow/lg`
- `effect/shadow/xl`
- `effect/shadow/floating-cta`
- `effect/shadow/floating-menu`
- `effect/shadow/floating-toast`
- `effect/shadow/floating-token-logo`
- `effect/shadow/glass-beta`
- `effect/shadow/glass-button-md`
- `effect/shadow/glass-button-lg`
- `effect/shadow/glass-card`
- `effect/shadow/token-main`

### Phase 4: Page `3285:437` spacing and radius token coverage

Actions completed:

- exact-match bindings were applied for existing spacing and radius tokens
- missing reusable primitives were added to the source token file and then applied in Figma:
  - `spacing/2`
  - `spacing/10`
  - `spacing/14`
  - `spacing/15`
  - `spacing/48`
  - `spacing/62`
  - `radius/xs`
- additional exact-match gap, padding, and radius bindings were applied on the page

Intentionally left as exceptions:

- board or showcase layout values such as `248`, `1151`, `56`, `7.778`
- fractional geometry values such as `0.508` and `0.762`
- a few mixed padding cases that would require semantic judgment instead of mechanical binding

Result:

- the page reached a stable state where almost all directly tokenizable structure values were covered
- remaining values are now explicit exceptions rather than unknown residue

### Phase 5: Showcase page readability cleanup

Scope:

- the same `组件Phase 1` page

Actions completed:

- normalized helper labels:
  - `父组件` -> `组件定义`
  - `子组件` -> `组合示例`

Result:

- the page now reads more clearly as a DS governance and review page

### Phase 6: Target component-page migration skeletons

Scope:

- create target pages without touching the Phase 0 and Phase 1 source pages

Target pages now holding migration skeletons:

- `原子组件/Navigation`
- `原子组件/Button`
- `原子组件/Modal`
- `原子组件/Toast+Dialog`
- `原子组件/Toggle`
- `原子组件/Backdrop`
- `业务组件/Error`

Page mapping now in place:

- `原子组件/Navigation`
  - `Nav`
  - `Token list`
  - `Menu`
  - `beta`
  - `Web nav`
  - `Mobile nav`
- `原子组件/Button`
  - `Button`
  - `Button with blur`
  - `Button-Web`
  - `Token function bar`
- `原子组件/Modal`
  - `Modal`
- `原子组件/Toast+Dialog`
  - `Toast`
  - `Toast-Web` as example
- `原子组件/Toggle`
  - `Toggle`
- `原子组件/Backdrop`
  - `Modal backdrop`
  - `Bkg`
- `业务组件/Error`
  - `Error` as a business example page

Result:

- Phase A and Phase B were established
- source pages `组件Phase 0` and `组件Phase 1` remained untouched during the migration skeleton work

## 3. Summary Of The Last 24 Hours

The work in the last 24 hours accomplished four meaningful outcomes:

1. The existing DS file stopped depending on stale remote variable bindings for the audited core component families.
2. The public API of the most important component sets became much more readable and maintainable.
3. The main governance page was brought to a much cleaner state for effect, spacing, radius, and showcase labeling.
4. The next-stage component pages were scaffolded without destroying the historical Phase 0 and Phase 1 working pages.

In practical terms, the file moved from "messy but partially structured" to "governable, inspectable, and ready for controlled component-page hardening."

## 4. Current Figma Token Schema Overview

Current source token file:

- `Iteration temp/source_token_v5.json`

### Top-level structure

The file currently uses this high-level schema:

- `Primitive`
- `Light`
- `Dark`
- `$themes`
- `$metadata`

### Primitive layer

The `Primitive` layer currently acts as the raw shared foundation.

High-level groups include:

- `primitive/color`
- `primitive/spacing`
- `primitive/size`
- `primitive/radius`
- `primitive/typography/family`
- `primitive/typography/weight`
- `primitive/typography/size`
- `primitive/typography/lineHeight`
- `primitive/typography/letterSpacing`

Approximate primitive token count:

- `100` total primitive tokens

Type distribution:

- `color`: `44`
- `dimension`: `35`
- `borderRadius`: `5`
- `fontFamilies`: `3`
- `fontWeights`: `3`
- `fontSizes`: `7`
- `lineHeights`: `2`
- `letterSpacing`: `1`

### Theme layers

Both `Light` and `Dark` currently use the same three-part structure:

- `semantic`
- `pattern`
- `component`

Each theme currently contains approximately:

- `114` token entries

### Semantic layer

The semantic layer is the main canonical layer for DS usage.

Top groups:

- `background`
- `text`
- `stroke`
- `border`
- `fill`
- `gradient`
- `status`
- `font`

Examples:

- `semantic/background/general`
- `semantic/text/core`
- `semantic/text/inverse`
- `semantic/stroke/icon_primary`
- `semantic/stroke/icon_inverse`
- `semantic/border/default`
- `semantic/fill/action`
- `semantic/fill/action_subtle`
- `semantic/font/heroTitle`

Interpretation:

- this is the layer that should drive most Figma variable binding and style decisions
- if a component property can be expressed semantically, this layer should usually win over raw primitive values

### Pattern layer

The pattern layer captures reusable composition-level aliases that are broader than a single property but narrower than a full component implementation.

Top groups:

- `pattern/surface`
- `pattern/modal`
- `pattern/list`

Examples:

- `pattern/surface/card/background`
- `pattern/surface/card/title`
- `pattern/modal/form/fieldBackground`
- `pattern/list/tokenItem/gap`

Interpretation:

- this layer is useful for repeated design motifs
- it is not always a native Figma-friendly layer
- it should be used carefully so it does not compete with the semantic layer for the same role

### Component layer

The component layer contains component-family-specific aliases.

Top groups:

- `component/mobileNav`
- `component/webNav`
- `component/modal`
- `component/button`
- `component/menu`
- `component/tokenList`

Examples:

- `component/button/primary/default/background`
- `component/button/primary/default/text`
- `component/mobileNav/primary/default/...`
- `component/webNav/default/signedIn/...`

Interpretation:

- this layer is practical for component-specific overrides and API-level defaults
- but it should not expand until it starts duplicating semantic responsibilities

### Current schema reading

The schema is currently best understood as:

1. `Primitive`
   - raw values
2. `Semantic`
   - canonical DS usage layer
3. `Pattern`
   - reusable composition aliases
4. `Component`
   - component-family-specific aliases

This means the file is not following a strict `Primitive + Semantic only` model.

That is acceptable for the current DS, but it creates a governance burden:

- `Semantic` should remain the default binding target
- `Pattern` should stay small and intentional
- `Component` should be justified only when a family-specific alias improves maintainability

## 5. Recommended Future Flows

The next question is not just how to maintain the DS in Figma, but how to use it across:

- design to code
- AI to code
- AI to design
- human designer editing and DS usage

The right answer is not one single flow. It should be a small set of coordinated flows sharing the same DS foundations.

### A. Design to Code

Goal:

- convert approved Figma components or pages into production implementation

Recommended flow:

1. Use the DS page or component page as the canonical design source
2. Use `figma-code-connect-components` for component-level mapping where the component API is stable
3. Use `figma-implement-design` for node-to-code translation when exact design fidelity matters
4. Validate the produced code against:
   - semantic token names
   - component property names
   - DS page screenshots

Best fit:

- mature component pages
- stable variants
- production implementation handoff

### B. AI to Code

Goal:

- have an agent generate or update production UI code from the current DS and Figma state

Recommended flow:

1. Treat the DS Figma file as the visual contract
2. Use `figma-implement-design` for node context and screenshot-backed translation
3. Use `figma-code-connect-components` where mapping exists so the agent resolves to the correct code components
4. Keep `source_token_v5.json` as the token source of truth for generated styling
5. Validate generated code back against the component pages, not against old showcase boards

Best fit:

- component implementation
- page implementation from stabilized component definitions
- code refactors where visual fidelity still matters

### C. AI to Design

Goal:

- have an agent extend or reorganize the DS or build new DS-backed pages in Figma

Recommended flow:

1. Use `figma-generate-library` to decide the correct phase and scope
2. Use `figma-use` for all incremental writes
3. Use `audit-design-system` before and after broad passes
4. Use `apply-design-system` if the task is reconnecting an existing page to the DS
5. Use `rad-spacing` only when spacing hierarchy is the actual problem

Best fit:

- component-page organization
- token/style cleanup
- DS-backed new page creation
- migration of legacy sections

### D. Human Designer Editing And DS Usage

Goal:

- let a human designer extend or consume the library without reintroducing drift

Recommended flow:

1. Edit from the new dedicated component pages, not from historical cleanup boards
2. Bind to `Semantic` first
3. Use `Pattern` only for deliberate repeated motifs
4. Use `Component` only when the alias is clearly component-specific
5. After significant edits, run:
   - a token drift check
   - a design-system audit
   - a page-level normalization pass if needed

Best fit:

- routine DS maintenance
- new variant authoring
- example curation
- small interaction or style improvements

### E. DS Rebuild Or Regeneration From Source

Goal:

- rebuild or refresh Figma foundations and components from a cleaner, more explicit source model

Recommended flow:

1. use `figma-create-design-system-rules` to formalize project rules first
2. use `cc-figma-tokens` when the token source is stable enough to become the canonical Figma variable layer
3. use `cc-figma-component` only after the token layer is stable and the component contract is explicit
4. use `sync-figma-token` afterward to verify parity rather than assuming the rebuild stayed aligned

Best fit:

- greenfield DS setup
- major library rebuild
- contract-first component regeneration

### F. New File Or Sandbox Work

Goal:

- create a clean workspace for experimentation, branch migration, or scratch DS reconstruction

Recommended flow:

1. use `figma-create-new-file` to create the new design file
2. if the goal is a new screen or page, use `figma-generate-design` or `edit-figma-design`
3. if the goal is a library rebuild, use `figma-generate-library` plus `figma-use`

Best fit:

- scratch rebuilds
- branch files for risky experiments
- concept work that should not happen directly in the main DS file

## 6. Recommended Unified Operating Model

If this DS is going to support both humans and AI reliably, use this operating model:

1. `source_token_v5.json` is the token source of truth
2. Figma `Semantic` variables are the default binding layer
3. dedicated component pages are the source of truth for component API and visual contract
4. Code Connect maps stable component pages to real code components
5. AI implementations should read from component pages and token schema, not from historical cleanup boards
6. human edits should happen on the dedicated DS pages first, then be re-audited

In short:

- tokens define values
- component pages define reusable UI contracts
- Figma audits catch drift
- Code Connect and design implementation flows bridge to code

## 7. Immediate Next Recommendation

The most effective next step is:

1. audit the newly scaffolded target pages one by one
2. normalize their internal layout and examples
3. decide which of those pages are now canonical edit surfaces
4. only then start formal design-to-code and AI-to-code mapping

This keeps the DS stable enough that later code generation is grounded in the right pages instead of in transitional cleanup boards.

---

## 中文翻译

### 1. 推荐的 Skill Workflow

这套 workflow 针对的是当前这个已有历史结构的 Figma DS 文件，而不是一个从零开始的全新库。

核心 skill 组合是：

- `figma-use`
- `figma-generate-library`
- `audit-design-system`
- `apply-design-system`
- `sync-figma-token`
- `rad-spacing`

它们分别承担：

- `figma-use`：Figma 读写执行
- `figma-generate-library`：阶段编排和治理顺序
- `audit-design-system`：发现 drift 和未系统化问题
- `apply-design-system`：页面或 section 级的接回设计系统
- `sync-figma-token`：code token 与 Figma variable 的一致性检查
- `rad-spacing`：间距、padding、gap 层级规范化

推荐的操作顺序：

1. 用 `figma-use` 做只读盘点
2. 用 `audit-design-system` 找系统化问题
3. 涉及 token 一致性时，用 `sync-figma-token` 先 dry-run
4. 用 `figma-use` 做 targeted writes
5. 页面或切片级调整时用 `apply-design-system`
6. 布局层级问题时用 `rad-spacing`
7. 最后再用 `figma-use` 做精修和验证

### 2. 主流程之外的完整 skill 覆盖

3 月 24 / 25 新增的 skill 比当前治理主循环更大，还包括：

- `cc-figma-tokens`
- `cc-figma-component`
- `figma-create-design-system-rules`
- `figma-code-connect-components`
- `figma-create-new-file`
- `figma-generate-design`
- `edit-figma-design`
- `multi-agent`

其中：

- `cc-figma-tokens`：适合从更干净的 code token source 重建 Figma variables
- `cc-figma-component`：适合在 contract 成熟时按 contract 生成或刷新组件
- `figma-create-design-system-rules`：适合生成项目级 DS 规则
- `figma-code-connect-components`：适合组件页稳定后做 code mapping
- `figma-create-new-file`：适合新建 sandbox / branch file
- `figma-generate-design`：适合生成完整页面或 screen
- `edit-figma-design`：适合文本驱动设计迭代
- `multi-agent`：适合并行分析和实现协作，不适合并行 Figma 写入

### 3. 过去 24 小时的时间线

#### Phase 0：基础层清理与绑定恢复

完成了：

- 本地变量 `scope` 规范化
- 本地变量 `WEB code syntax` 规范化
- 创建缺失 token `Semantic/text/inverse`
- 将该 token 回填到 `source_token_v5.json`
- 清理多个核心 family 的 legacy binding
- 把核心 typography 使用迁回本地 text styles

结果：

- 核心组件家族审计后的 residual nonlocal bindings 为 `0`

#### Phase 0.5：Token schema 增补

新增并同步到 Figma 和 `source_token_v5.json` 的 token 包括：

- `Semantic/text/inverse`
- `Semantic/fill/action`
- `Semantic/fill/action_subtle`
- `Semantic/stroke/logo`
- `Semantic/stroke/icon_inverse`

#### Phase 1：组件 API 清理

清理了：

- `Nav` 的 `Property 1` -> `Variant`
- `Token list` 的 `Property 1` -> `State`
- `Menu` 的 `Property 1` -> `Status`
- `Mobile nav` 的 `Level` values 统一
- `Breadcrumb` 的 `Hierarchy` 拼写
- `Button-Web` 的 boolean property 命名
- `Modal` 的 public property API

结果：

- 主要组件家族在 property panel 中可读性显著提升

#### Phase 2：样式治理审查

确认了：

- 本地 text styles 已比较 canonical
- gradient styles 结构可接受
- `component/button/primary/fill` 和 `component/button/primary/stroke` 继续保留
- 全局 shadow scale 结构清晰

#### Phase 3：页面 `3285:437` 的 effect-style 治理

完成了：

- 建立统一 `effect/...` 命名空间
- 对重复 blur / shadow recipe 建 style 并回绑

结果：

- 页面上 `59` 个 effect-bearing nodes 全部 styled
- `0` 个 bare effects

#### Phase 4：页面 `3285:437` 的 spacing / radius token 覆盖

完成了：

- 现有 spacing / radius exact-match 回绑
- 新增 primitive：
  - `spacing/2`
  - `spacing/10`
  - `spacing/14`
  - `spacing/15`
  - `spacing/48`
  - `spacing/62`
  - `radius/xs`
- 将它们同步到 source token 并在页面中应用

刻意保留的例外：

- board/showcase 布局值
- fractional geometry
- 需要语义判断的 mixed padding

#### Phase 5：展示页可读性整理

完成了：

- `父组件` -> `组件定义`
- `子组件` -> `组合示例`

#### Phase 6：目标组件页 migration skeleton

已建立目标页：

- `原子组件/Navigation`
- `原子组件/Button`
- `原子组件/Modal`
- `原子组件/Toast+Dialog`
- `原子组件/Toggle`
- `原子组件/Backdrop`
- `业务组件/Error`

并完成了主要 family 的页面映射。

### 4. 过去 24 小时总结

这轮工作带来的主要结果是：

1. 核心组件家族摆脱了旧 remote binding
2. 关键 component API 更清晰、更可维护
3. `组件Phase 1` 页在 effect、spacing、radius、label 上变得更整洁
4. 新的目标组件页已完成 skeleton 迁移，但没有破坏历史治理页

文件整体从“messy 但部分有结构”推进到了“可以治理、可以检查、适合继续扶正”的状态。

### 5. 当前 token schema 概览

当前源 token 文件是：

- `Iteration temp/source_token_v5.json`

顶层结构包括：

- `Primitive`
- `Light`
- `Dark`
- `$themes`
- `$metadata`

#### Primitive 层

作为原始值基础层，包含：

- `primitive/color`
- `primitive/spacing`
- `primitive/size`
- `primitive/radius`
- `primitive/typography/*`

当前大约有：

- `100` 个 primitive token

#### Theme 层

`Light` 和 `Dark` 都由三部分组成：

- `semantic`
- `pattern`
- `component`

每个 theme 当前约有：

- `114` 个 token 条目

#### Semantic 层

这是主要 canonical DS binding layer，包含：

- background
- text
- stroke
- border
- fill
- gradient
- status
- font

这是绝大多数 Figma variable binding 和 style 决策的主层。

#### Pattern 层

这是组合级 alias 层，适合：

- card surface
- modal form
- list item 等重复模式

它有价值，但不应和 semantic 层争夺相同职责。

#### Component 层

这是 family-specific alias 层，当前主要面向：

- mobileNav
- webNav
- modal
- button
- menu
- tokenList

它适合组件家族默认值，但不应无限膨胀。

### 6. 未来推荐 workflow

这份文档最后一部分讨论了治理之后的 DS 如何支持：

- Design to Code
- AI to Code
- AI to Design
- Human designer editing

核心原则是：

1. `source_token_v5.json` 是 token source of truth
2. Figma `Semantic` variable 是默认 binding layer
3. dedicated component pages 是 component API 和视觉契约的 source of truth
4. Code Connect 在 canonical pages 稳定后再接入
5. AI 和 human 的编辑都应围绕 canonical component pages 展开，而不是继续围绕历史 cleanup boards

### 7. 立即推荐的下一步

最有效的下一步不是继续做泛 cleanup，而是：

1. 逐页审计新建的目标组件页
2. 规范它们的内部布局和 examples
3. 明确哪些页面是 canonical edit surfaces
4. 只有在那之后再进入正式的 Figma to Code / AI to Code 映射

---

# Figma 设计系统工作流、时间轴与 Token 架构

日期：2026-03-26

目标 Figma 文件：
`DBQdb8ymhIfTPS9GmcTqaR`

相关源 Token 文件：
`Iteration temp/source_token_v5.json`

## 1. 推荐的技能工作流

此工作流针对 Figma 设计系统文件的当前状态：这是一个已有的库，包含变量、样式、组件集、展示页以及页面本地清理历史。

### 核心技能组

- `figma-use`
  - 每个 `use_figma` 读写操作的强制基础层
  - 用于所有 Figma 插件 API 的检查、变更、迁移和页面结构重新调整
- `figma-generate-library`
  - 用作设计系统工作的编排层
  - 定义了正确的阶段顺序：探索 -> 基础 -> 文件结构 -> 组件 -> 质量保证 (QA)
- `audit-design-system`
  - 用于对页面、切片或组件家族进行只读审计
  - 最适合发现偏差（drift）：本地包装器、缺失绑定、重复的自定义框架、原始值
- `apply-design-system`
  - 当现有页面或切片需要重新挂载到系统原语或根据规范组件重新组织时使用
  - 不要用于单个微小的修复
- `sync-figma-token`
  - 用于代码 Token 与 Figma 变量的一致性同步
  - 务必先进行干跑（dry-run），然后停止，最后在单独的步骤中应用
- `rad-spacing`
  - 当主要问题是布局层级、自动布局间距或填充/间隙规范化时使用

### 本仓库中各项技能的用途

#### `figma-use`

每当任务涉及以下内容时使用：

- 检查页面、组件集、变量、样式或节点树
- 写入新变量或样式
- 重命名组件属性和变体（variants）
- 克隆或移动组件到新页面
- 将变量绑定到填充、描边、效果、间距或圆角

实际上，这是执行引擎。

#### `figma-generate-library`

使用此工具确保工作顺序正确：

- 首先检查并锁定范围
- 然后清理或扩展基础
- 接着组织文件结构
- 随后强化组件页面
- 最后进行 QA

实际上，这是治理和排序层。

#### `audit-design-system`

在调整阶段之前使用，以回答以下问题：

- 该节点是正式的组件实例还是本地构建的
- 是否有重复的自定义结构需要组件化
- Token 和样式是否实际绑定
- 是否存在变体偏差或页面本地的不一致

实际上，这是诊断层。

#### `apply-design-system`

当范围已明确且足够广泛，足以支持切片级的重写或规范化操作时使用。

典型用例：

- 将页面切片重连至规范库组件
- 根据正式组件定义重建展示区域
- 将混乱的页面（包含混合本地框架）转换为由系统支撑的结构

实际上，这是页面级的修复层。

#### `sync-figma-token`

仅用于 Token 一致性。

典型检查项目：

- Token 存在于代码中但不存在于 Figma 中
- 别名（alias）目标不同
- 值在不同模式下存在差异
- 范围（scopes）或代码语法错误

实际上，这是 Token 治理层。

#### `rad-spacing`

当页面结构正确但由于间隙和填充不一致导致层级在视觉上较为混乱时使用。

实际上，这是布局规范化层。

### 推荐的操作流程

针对本仓库和此 Figma 文件，实际流程应为：

1. 使用 `figma-use` 进行只读盘点
2. 使用 `audit-design-system` 进行设计系统偏差诊断
3. 涉及 Token 一致性时，使用 `sync-figma-token` 进行干跑
4. 使用 `figma-use` 进行有针对性的写入
5. 当调整规模达到切片级而非节点级时，使用 `apply-design-system`
6. 当间距层级需要规范化时，使用 `rad-spacing`
7. 再次使用 `figma-use` 进行最终的精确修复和验证

### 对全部新技能的覆盖说明

3 月 24 日和 3 月 25 日新增的技能集合比当前这条设计系统治理主循环更大。下面这些技能也应该被明确覆盖，但并不是所有技能都属于默认的清理流程。

#### 属于设计系统相邻工作流的技能

- `cc-figma-tokens`
  - 当目标是根据更干净的代码 Token 源来构建或重建 Figma 变量集合时使用
  - 更适合受控的 Token 库重建，而不适合在一个已经较乱的文件上做页面级局部清理
- `cc-figma-component`
  - 在 Figma 中的 Token 集合已经稳定之后使用
  - 适用于组件 contract 已足够成熟，需要按 contract 结构生成或刷新组件家族的场景
- `figma-create-design-system-rules`
  - 用于生成项目级设计系统规则和运行约定
  - 适合需要明确治理文档或 `AGENTS.md` 规则段落时使用
- `figma-code-connect-components`
  - 这个技能已经与当前设计系统相关，但它属于组件页稳定之后的下游环节
  - 当组件 API 和规范页面已经稳定，可以映射到代码时使用

#### 有明确适用场景，但不属于默认清理循环的技能

- `figma-create-new-file`
  - 当需要新的设计系统沙盒、分支文件或草稿重建文件时使用
  - 当前这次原地治理不需要它，因为目标文件已经存在
- `figma-generate-design`
  - 当需要从代码或产品描述在 Figma 中生成完整 screen 或 view 时使用
  - 更适合在设计系统足够稳定、可以作为导入原语和组件来源之后使用
- `edit-figma-design`
  - 当设计工作主要由文本驱动，而不是 Token / 组件治理任务时使用
  - 适用于探索性概念设计或根据文字反馈迭代某个具体页面
- `multi-agent`
  - 适合用在并行只读分析、规划协作或代码侧实现协作上
  - 不要用于并行 `use_figma` 写入；Figma 修改仍必须保持串行

#### 这些补充技能在整体图景中的位置

完整的理解方式应为：

1. `figma-create-design-system-rules`
   - 定义项目规则
2. `cc-figma-tokens`
   - 在需要时构建或重建设计系统的规范 Token 集合
3. `cc-figma-component`
   - 在需要时按 contract 生成或刷新组件
4. 主治理循环
   - `figma-use`
   - `figma-generate-library`
   - `audit-design-system`
   - `apply-design-system`
   - `sync-figma-token`
   - `rad-spacing`
5. 下游生产工作流
   - `figma-code-connect-components`
   - `figma-generate-design`
   - `edit-figma-design`
   - `multi-agent`
   - `figma-create-new-file`

### 推荐的方案模板

在文件中的任何页面或家族上应用此方案：

1. 检查 (Inspect)
   - 页面结构
   - 组件集和实例
   - 变量、样式和现有约定
2. 审计 (Audit)
   - Token/样式绑定覆盖率
   - 系统偏差
   - 重复的本地结构
3. 决定范围 (Decide scope)
   - Token 修复
   - 页面清理
   - 家族清理
   - 间距规范化
4. 增量应用 (Apply incrementally)
   - 每次处理一个页面或一个家族
   - 每次 `use_figma` 调用执行一个写入步骤
5. 重新审计 (Re-audit)
   - 验证无视觉回归
   - 验证无明显的残留偏差

## 2. 过去 24 小时的工作时间轴

此时间轴总结了过去 24 小时内 Figma 文件中完成的实际工作。它按执行阶段组织，而非挂钟时间戳，因为工作是按一系列引导式清理步骤进行的。

### 阶段 0：基础清理与 Token 绑定恢复

范围：

- 当前本地变量模型
- 核心组件页
- 各个主要组件家族的绑定清理

已完成动作：

- 规范化本地变量的 `scope`
- 规范化本地变量的 `WEB code syntax`
- 创建了缺失的语义 Token `Semantic/text/inverse`
- 将该 Token 回填至 `Iteration temp/source_token_v5.json`
- 将明显的旧版远程颜色绑定重新绑定到当前的本地语义层
- 清理了以下组件中最后的非规范绑定残留：
  - `Button`
  - `Button-Web`
  - `Modal`
  - `Nav`
  - `Web nav`
  - `Mobile nav`
  - `Menu`
  - `Token list`
  - `Toast`
  - `Toggle`
  - `Breadcrumb`
  - `Bkg`
- 将核心排版使用迁移回本地文本样式

结果：

- 在覆盖到的主要组件家族中，审计出的残留非本地绑定降至 `0`

### 阶段 0.5：Token 架构扩充

由于现有的设计系统界面需要，但源 Token 架构尚未提供，因此生成了以下缺失的语义 Token：

- `Semantic/text/inverse`
- `Semantic/fill/action`
- `Semantic/fill/action_subtle`
- `Semantic/stroke/logo`
- `Semantic/stroke/icon_inverse`

这些 Token 已在 Figma 中创建，并同步添加至 `Iteration temp/source_token_v5.json`。

### 阶段 1：组件 API 清理

范围：

- 公共组件 API 的可读性
- 变体轴（variant axis）命名
- 布尔属性（boolean property）命名
- 拼写错误清理

已完成动作：

- `Nav`
  - `Property 1` -> `Variant`
- `Token list`
  - `Property 1` -> `State`
- `Menu`
  - `Property 1` -> `Status`
- `Mobile nav`
  - 变体汇聚为 `Level=Top nav` 和 `Level=Secondary nav`
- `Breadcrumb`
  - `Hiearachy` -> `Hierarchy`
- `Button-Web`
  - 布尔属性重命名为 `Show blur` 和 `Show description`
- `Modal`
  - 围绕可读文本和平台字段重新设计了公共属性 API
  - 移除了陈旧未使用的文本属性

结果：

- 当前高价值组件家族在属性面板中的可读性显著提升
- 无需进行大规模重建

### 阶段 2：样式治理审查

范围：

- 本地文本样式
- 本地填充样式
- 本地效果样式

发现：

- 本地文本样式已处于良好的规范状态，并与语义字体模型对齐
- 本地渐变样式结构已足够完善
- `component/button/primary/fill` 和 `component/button/primary/stroke` 被有意保留为特定组件的填充样式
- 全局阴影阶梯结构清晰

结果：

- 阶段 2 以审计开始，而非破坏性的重写

### 阶段 3：页面 `3285:437` 效果样式治理

目标页面：

- `3285:437` / `组件Phase 1: Component Schema Cleanup`

已完成动作：

- 保留了 `component/button/primary/fill`
- 保留了 `component/button/primary/stroke`
- 引入并应用了统一的 `effect/...` 命名空间
- 针对重复的效果配方创建了页面本地的模糊和阴影效果样式

页面上的最终效果状态：

- `59` 个带有效果的节点
- `59` 个已设置样式的节点
- `0` 个裸效果（未绑定样式）

页面上的最终效果命名空间：

- `effect/blur/background-none`
- `effect/blur/background-md`
- `effect/blur/layer-xs`
- `effect/blur/layer-sm`
- `effect/blur/layer-md`
- `effect/blur/layer-lg`
- `effect/shadow/sm`
- `effect/shadow/md`
- `effect/shadow/lg`
- `effect/shadow/xl`
- `effect/shadow/floating-cta`
- `effect/shadow/floating-menu`
- `effect/shadow/floating-toast`
- `effect/shadow/floating-token-logo`
- `effect/shadow/glass-beta`
- `effect/shadow/glass-button-md`
- `effect/shadow/glass-button-lg`
- `effect/shadow/glass-card`
- `effect/shadow/token-main`

### 阶段 4：页面 `3285:437` 间距与圆角 Token 覆盖

已完成动作：

- 对现有的间距和圆角 Token 应用了精确匹配绑定
- 将缺失的可复用原语添加至源 Token 文件并在 Figma 中应用：
  - `spacing/2`
  - `spacing/10`
  - `spacing/14`
  - `spacing/15`
  - `spacing/48`
  - `spacing/62`
  - `radius/xs`
- 在页面上应用了额外的精确匹配间隙（gap）、填充（padding）和圆角绑定

有意保留的例外情况：

- 画板或展示页布局值，如 `248`, `1151`, `56`, `7.778`
- 小数几何值，如 `0.508` 和 `0.762`
- 少数混合填充案例，这些需要语义判断而非机械绑定

结果：

- 页面达到了稳定状态，几乎所有可直接 Token 化的结构值均已覆盖
- 剩余值现在是明确的例外，而非未知的残留

### 阶段 5：展示页可读性清理

范围：

- 同一 `组件Phase 1` 页面

已完成动作：

- 规范化了辅助标签：
  - `父组件` -> `组件定义`
  - `子组件` -> `组合示例`

结果：

- 该页面作为设计系统治理和审查页的可读性变得更清晰

### 阶段 6：目标组件页迁移骨架

范围：

- 创建目标页面，不改动阶段 0 和阶段 1 的源页面

现持有迁移骨架的目标页面：

- `原子组件/Navigation`
- `原子组件/Button`
- `原子组件/Modal`
- `原子组件/Toast+Dialog`
- `原子组件/Toggle`
- `原子组件/Backdrop`
- `业务组件/Error`

现有的页面映射计划：

- `原子组件/Navigation`
  - `Nav`
  - `Token list`
  - `Menu`
  - `beta`
  - `Web nav`
  - `Mobile nav`
- `原子组件/Button`
  - `Button`
  - `Button with blur`
  - `Button-Web`
  - `Token function bar`
- `原子组件/Modal`
  - `Modal`
- `原子组件/Toast+Dialog`
  - `Toast`
  - `Toast-Web` (作为示例)
- `原子组件/Toggle`
  - `Toggle`
- `原子组件/Backdrop`
  - `Modal backdrop`
  - `Bkg`
- `业务组件/Error`
  - `Error` (作为业务示例页面)

结果：

- 确立了 A 阶段和 B 阶段
- 在迁移骨架工作期间，源页面 `组件Phase 0` 和 `组件Phase 1` 保持不变

## 3. 过去 24 小时工作总结

过去 24 小时的工作达成了四个具有意义的成果：

1. 现有的设计系统文件停止依赖针对核心组件家族的陈旧远程变量绑定。
2. 最重要组件集的公共 API 变得更具可读性和可维护性。
3. 主要治理页面在效果、间距、圆角和展示标签方面达到了更整洁的状态。
4. 在不破坏历史阶段 0 和阶段 1 工作页面的情况下，搭建了下一阶段组件页面的支架。

从实际意义上讲，文件已从“混乱但部分结构化”转变为“可治理、可检查，并为受控的组件页强化做好了准备”。

## 4. 当前 Figma Token 架构概览

当前源 Token 文件：

- `Iteration temp/source_token_v5.json`

### 顶层结构

该文件目前采用以下高层架构：

- `Primitive`（原语）
- `Light`（浅色模式）
- `Dark`（深色模式）
- `$themes`（主题）
- `$metadata`（元数据）

### 原语层 (Primitive layer)

`Primitive` 层目前作为原始共享基础。

高层分组包括：

- `primitive/color` (颜色)
- `primitive/spacing` (间距)
- `primitive/size` (尺寸)
- `primitive/radius` (圆角)
- `primitive/typography/family` (字体家族)
- `primitive/typography/weight` (字重)
- `primitive/typography/size` (字号)
- `primitive/typography/lineHeight` (行高)
- `primitive/typography/letterSpacing` (字间距)

原语 Token 的大约数量：

- 总计约 `100` 个原语 Token

类型分布：

- 颜色 (`color`): `44`
- 维度 (`dimension`): `35`
- 圆角 (`borderRadius`): `5`
- 字体家族 (`fontFamilies`): `3`
- 字重 (`fontWeights`): `3`
- 字号 (`fontSizes`): `7`
- 行高 (`lineHeights`): `2`
- 字间距 (`letterSpacing`): `1`

### 主题层 (Theme layers)

`Light` 和 `Dark` 目前都采用相同的三部分结构：

- `semantic` (语义层)
- `pattern` (模式层)
- `component` (组件层)

每个主题目前包含大约：

- `114` 个 Token 条目

### 语义层 (Semantic layer)

语义层是设计系统使用的主要规范层。

核心分组：

- `background` (背景)
- `text` (文本)
- `stroke` (描边)
- `border` (边框)
- `fill` (填充)
- `gradient` (渐变)
- `status` (状态)
- `font` (字体)

示例：

- `semantic/background/general`
- `semantic/text/core`
- `semantic/text/inverse`
- `semantic/stroke/icon_primary`
- `semantic/stroke/icon_inverse`
- `semantic/border/default`
- `semantic/fill/action`
- `semantic/fill/action_subtle`
- `semantic/font/heroTitle`

解读：

- 这是驱动大多数 Figma 变量绑定和样式决策的层级
- 如果一个组件属性可以用语义方式表达，该层级通常应优于原始原语值

### 模式层 (Pattern layer)

模式层捕捉可复用的组合级别别名，这些别名比单个属性更宽泛，但比完整的组件实现更狭窄。

核心分组：

- `pattern/surface` (表面)
- `pattern/modal` (弹窗)
- `pattern/list` (列表)

示例：

- `pattern/surface/card/background`
- `pattern/surface/card/title`
- `pattern/modal/form/fieldBackground`
- `pattern/list/tokenItem/gap`

解读：

- 此层级对于重复的设计模式非常有用
- 它并不总是原生 Figma 友好的层级
- 应谨慎使用，以免在相同角色上与语义层产生冲突

### 组件层 (Component layer)

组件层包含特定于组件家族的别名。

核心分组：

- `component/mobileNav`
- `component/webNav`
- `component/modal`
- `component/button`
- `component/menu`
- `component/tokenList`

示例：

- `component/button/primary/default/background`
- `component/button/primary/default/text`
- `component/mobileNav/primary/default/...`
- `component/webNav/default/signedIn/...`

解读：

- 此层级对于特定组件的覆盖和 API 级别的默认值非常实用
- 但它不应随意扩展，直到它开始与语义职责重复

### 当前架构评估

该架构目前最好的理解方式是：

1. `Primitive` (原语)
   - 原始值
2. `Semantic` (语义)
   - 规范的设计系统使用层
3. `Pattern` (模式)
   - 可复用的组合别名
4. `Component` (组件)
   - 特定于组件家族的别名

这意味着该文件并未遵循严格的 `Primitive + Semantic Only` 模型。

这对于当前的设计系统是可以接受的，但会带来治理负担：

- `Semantic` 应保持作为默认的绑定目标
- `Pattern` 应保持小规模且具有明确目的性
- `Component` 仅在特定家族的别名能显著提高可维护性时才具合理性

## 5. 推荐的未来工作流

接下来的问题不仅是如何在 Figma 中维护设计系统，还包括如何在以下场景中使用它：

- 设计到代码 (Design to code)
- AI 到代码 (AI to code)
- AI 到设计 (AI to design)
- 人类设计师编辑与设计系统使用

正确的答案不是单一的工作流，而应该是一组基于相同设计系统基础的协同流。

### A. 设计到代码

目标：

- 将批准的 Figma 组件或页面转换为生产环境实现

推荐流程：

- 将设计系统页面或组件页面用作规范设计源
- 在组件 API 稳定的情况下，使用 `figma-code-connect-components` 进行组件级映射
- 当精确的设计还原度至关重要时，使用 `figma-implement-design` 进行节点到代码的转换
- 根据以下标准验证生成的代码：
  - 语义 Token 名称
  - 组件属性名称
  - 设计系统页面截图

最佳适用：

- 成熟的组件页面
- 稳定的变体
- 生产实现交付

### B. AI 到代码

目标：

- 让 Agent 根据当前的设计系统和 Figma 状态生成或更新生产环境 UI 代码

推荐流程：

- 将设计系统 Figma 文件视为视觉契约
- 使用 `figma-implement-design` 获取节点上下文和基于截图的转换
- 在存在映射的地方使用 `figma-code-connect-components`，以便 Agent 解析到正确的代码组件
- 将 `source_token_v5.json` 保留为生成样式的 Token 事实来源
- 根据组件页面验证生成的代码，而非依据旧的展示看板

最佳适用：

- 组件实现
- 基于稳固组件定义的页面实现
- 视觉还原度仍然重要的代码重构

### C. AI 到设计

目标：

- 让 Agent 扩展或重新组织设计系统，或在 Figma 中构建新的基于设计系统的页面

推荐流程：

- 使用 `figma-generate-library` 决定正确的阶段和范围
- 使用 `figma-use` 进行所有增量写入
- 在大规模操作前后使用 `audit-design-system`
- 如果任务是将现有页面重新连接到设计系统，使用 `apply-design-system`
- 仅当间距层级是实际问题时使用 `rad-spacing`

最佳适用：

- 组件页组织
- Token/样式清理
- 基于设计系统的新页面创建
- 遗留切片的迁移

### D. 人类设计师编辑与设计系统使用

目标：

- 让人类设计师扩展或消费库文件，且不引入偏差

推荐流程：

- 从新的专用组件页面进行编辑，而非从历史清理看板
- 优先绑定到 `Semantic` 层
- 仅针对深思熟虑的重复模式使用 `Pattern` 层
- 仅当别名明确属于特定组件时使用 `Component` 层
- 在进行重大编辑后，运行：
  - Token 偏差检查
  - 设计系统审计
  - 如果需要，进行页面级规范化操作

最佳适用：

- 例行设计系统维护
- 新变体创作
- 示例整理
- 细微的交互或样式改进

### E. 基于源模型的设计系统重建或再生成

目标：

- 根据更清晰、更显式的源模型，重建或刷新 Figma 中的基础层和组件

推荐流程：

1. 先用 `figma-create-design-system-rules` 固化项目规则
2. 当 Token 源已经足够稳定，可以作为 Figma 变量的规范层时，使用 `cc-figma-tokens`
3. 只有在 Token 层稳定且组件 contract 明确之后，才使用 `cc-figma-component`
4. 完成后再使用 `sync-figma-token` 验证一致性，而不是假设重建天然保持对齐

最佳适用：

- 全新设计系统搭建
- 大规模库重建
- 以 contract 为中心的组件再生成

### F. 新文件或沙盒工作流

目标：

- 为实验、分支迁移或草稿式设计系统重建创建干净的工作空间

推荐流程：

1. 使用 `figma-create-new-file` 创建新的设计文件
2. 如果目标是生成新页面或新 screen，则使用 `figma-generate-design` 或 `edit-figma-design`
3. 如果目标是重建组件库，则使用 `figma-generate-library` 搭配 `figma-use`

最佳适用：

- 草稿重建
- 高风险实验的分支文件
- 不应直接在主设计系统文件中进行的概念设计

## 6. 推荐的统一运行模型

如果要让此设计系统可靠地支持人类和 AI，请采用以下运行模型：

1. `source_token_v5.json` 是 Token 的事实来源
2. Figma `Semantic` 变量是默认绑定层
3. 专用组件页面是组件 API 和视觉契约的事实来源
4. Code Connect 将稳定的组件页面映射到真实的代码组件
5. AI 实现应从组件页面和 Token 架构读取，而非从历史清理看板读取
6. 人类编辑应首先在专用设计系统页面上进行，然后重新进行审计

简而言之：

- Token 定义值
- 组件页面定义可复用的 UI 契约
- Figma 审计捕捉偏差
- Code Connect 和 design implementation flows 负责连接到代码

## 7. 立即执行的后续建议

最有效的下一步是：

1. 逐一审计新搭建的目标页面支架
2. 规范化其内部布局和示例
3. 确定其中哪些页面现在是规范的编辑表面
4. 只有在那之后才开始正式的设计到代码和 AI 到代码映射

这能保持设计系统足够稳定，从而使后续的代码生成植根于正确的页面，而非过渡性的清理看板。
