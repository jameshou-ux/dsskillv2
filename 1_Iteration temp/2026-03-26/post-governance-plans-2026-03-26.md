# Figma DS Post-Governance Plans

Date: 2026-03-26

Target Figma file:
`DBQdb8ymhIfTPS9GmcTqaR`

Related source token file:
`Iteration temp/source_token_v5.json`

## 1. Goal After DS Governance

Once the DS cleanup and page hardening work is stable, the next question is how this DS should operate across design, AI, and engineering workflows.

The answer should not be one single flow. It should be a coordinated operating model across four main scenarios:

- Figma to Code
- AI to Figma
- AI to Code
- Human designer with Figma

## 2. Figma to Code

### Goal

Translate approved Figma components or pages into production implementation.

### Recommended flow

1. Use canonical DS component pages as the design source
2. Ensure component property APIs are stable
3. Use `figma-code-connect-components` where component-to-code mapping is mature
4. Use `figma-implement-design` when exact node-to-code fidelity matters
5. Validate the implementation against:
   - semantic token names
   - component property names
   - DS page screenshots

### Requirements before this works well

- canonical component pages must exist
- historical cleanup boards should not be the primary handoff surface
- token semantics should be stable enough that code can trust them

## 3. AI to Figma

### Goal

Have an agent extend, reorganize, or generate DS-backed Figma work.

### Recommended flow

1. Use `figma-generate-library` to choose the right phase
2. Use `figma-use` for incremental Figma writes
3. Use `audit-design-system` before and after broad passes
4. Use `apply-design-system` when reconnecting existing page sections to the DS
5. Use `rad-spacing` when spacing hierarchy needs normalization
6. Use `figma-generate-design` or `edit-figma-design` only when the task is new screen creation rather than DS cleanup

### Requirements before this works well

- target pages should be clear enough that AI is not editing historical cleanup boards by mistake
- canonical token semantics should already be understood
- governance rules should be explicit

## 4. AI to Code

### Goal

Have an agent generate or update production UI code from the current DS and Figma state.

### Recommended flow

1. Treat canonical DS component pages as the visual contract
2. Use `figma-implement-design` to extract node context and screenshots
3. Use `figma-code-connect-components` when stable code mappings exist
4. Keep `source_token_v5.json` as the token source of truth
5. Validate generated code against canonical DS pages rather than against historical cleanup boards

### Requirements before this works well

- canonical component pages should be stable
- code mappings should be trustworthy
- the DS should no longer be in a transitional naming state

## 5. Human Designer With Figma

### Goal

Allow human designers to use and extend the DS without reintroducing drift.

### Recommended flow

1. Edit on canonical component pages, not on historical cleanup pages
2. Bind to `Semantic` by default
3. Use `Pattern` only when a repeated composition genuinely deserves it
4. Use `Component` aliases only when the family-specific alias clearly improves maintainability
5. After substantial edits, run:
   - token drift review
   - design-system audit
   - page normalization if needed

### Requirements before this works well

- canonical edit surfaces should be explicitly named and socially agreed
- governance pages should remain visible but clearly secondary

## 6. Where Contract-Driven Flows Fit Later

The DS does not need to become contract-driven everywhere immediately. But after governance, some families may become ready for stronger generation paths.

### When to introduce `cc-figma-tokens`

Use it when:

- the code-side token source is stable
- the team wants a stricter `Primitives + Semantic` import pipeline
- token governance should be more compiler-like and less manual

### When to introduce `cc-figma-component`

Use it when:

- a component family already has a reliable contract
- the team accepts regenerate-style refreshes
- a component should be derived from contract rather than maintained manually

### When not to use `cc-*` yet

Do not lead with it when:

- the DS file is still structurally messy
- canonical component pages are still being established
- the design team is still deciding the public API in Figma

## 7. Recommended Operating Model

The most stable long-term model for this DS is:

1. `source_token_v5.json` remains the token source of truth
2. Figma `Semantic` variables remain the default binding layer
3. dedicated component pages become the component source of truth
4. historical cleanup boards remain governance references
5. Code Connect is added after canonical pages stabilize
6. contract-driven regeneration is introduced only for mature families

## 8. Recommended Next Phase

The next meaningful phase after governance is page canonization, not immediate code generation.

Recommended order:

1. harden the target component pages
2. decide which pages are canonical edit surfaces
3. document the handoff rule:
   - canonical component page = handoff surface
   - Phase 0 / Phase 1 page = governance history
4. then begin:
   - Figma to Code
   - AI to Code
   - AI to Figma

## 9. Short Conclusion

The DS is now close to being operational, but the key transition is still ahead:

- from cleanup boards
- to canonical component pages

Once that transition is complete, the file can support all four workflows much more safely:

- Figma to Code
- AI to Figma
- AI to Code
- Human designer with Figma

---

## 中文翻译

### 1. DS 治理之后的目标

当 DS cleanup 和页面硬化工作稳定之后，下一步的问题就不再只是“如何清理 Figma”，而是这套 DS 如何支持设计、AI 和工程协作。

这里不应该只有一条流程，而应该有一套覆盖四个主要场景的协同 operating model：

- Figma to Code
- AI to Figma
- AI to Code
- Human designer with Figma

### 2. Figma to Code

目标：

- 把经过确认的 Figma 组件或页面落成生产实现

推荐流程：

1. 用 canonical DS component pages 作为设计源
2. 确保 component property API 已稳定
3. 在组件到代码映射成熟时使用 `figma-code-connect-components`
4. 当要求高保真 node-to-code 时使用 `figma-implement-design`
5. 用以下内容做回查：
   - semantic token names
   - component property names
   - DS page screenshots

前提要求：

- 必须已有 canonical component pages
- 历史 cleanup boards 不能再作为主 handoff surface
- token semantics 必须足够稳定，代码侧才能信任

### 3. AI to Figma

目标：

- 让 agent 扩展、重组或生成基于 DS 的 Figma 内容

推荐流程：

1. 用 `figma-generate-library` 选择正确阶段
2. 用 `figma-use` 做增量写入
3. 在较大改动前后运行 `audit-design-system`
4. 页面或 section 需要重新接回 DS 时使用 `apply-design-system`
5. 层级间距有问题时使用 `rad-spacing`
6. 只有在做新 screen 创建而不是 DS cleanup 时，才用 `figma-generate-design` 或 `edit-figma-design`

前提要求：

- target pages 已足够清晰，AI 不会误改历史治理页
- canonical token semantics 已经较明确
- governance rules 已显式化

### 4. AI to Code

目标：

- 让 agent 基于当前 DS 和 Figma 状态生成或更新生产 UI 代码

推荐流程：

1. 把 canonical DS component pages 当成视觉契约
2. 用 `figma-implement-design` 提取节点上下文和截图
3. 当 code mapping 稳定时，用 `figma-code-connect-components`
4. 保持 `source_token_v5.json` 作为 token source of truth
5. 用 canonical DS pages 验证生成代码，而不是拿历史 cleanup boards 做依据

前提要求：

- canonical component pages 已稳定
- code mappings 值得信任
- DS 不再处于命名和结构的过渡态

### 5. Human Designer With Figma

目标：

- 让设计师能在 Figma 里继续使用和扩展 DS，同时不重新引入 drift

推荐流程：

1. 在 canonical component pages 上编辑，而不是在历史 cleanup pages 上编辑
2. 默认优先绑定到 `Semantic`
3. 只有当某种重复组合确实值得沉淀时才用 `Pattern`
4. 只有当 family-specific alias 明显提升可维护性时才用 `Component`
5. 较大编辑后做：
   - token drift review
   - design-system audit
   - 如有需要再做 page normalization

前提要求：

- canonical edit surfaces 需要明确命名并形成团队共识
- governance pages 仍应保留，但角色要更清楚地退居第二层

### 6. contract-driven 流程之后如何接入

这套 DS 不需要一开始就全面 contract-driven，但在治理稳定后，某些 family 可以逐步进入更强的生成路径。

#### 何时引入 `cc-figma-tokens`

适合在以下情况下引入：

- code-side token source 已稳定
- 团队想要更严格的 `Primitives + Semantic` 导入管线
- token governance 想更像 compiler，而不是长期手工维护

#### 何时引入 `cc-figma-component`

适合在以下情况下引入：

- 某个 component family 已有可靠 contract
- 团队接受 regenerate-style refresh
- 某个组件更适合由 contract 派生，而不是长期纯手工维护

#### 何时暂时不要引入 `cc-*`

不要在这些状态下贸然用它：

- DS 文件整体还比较 messy
- canonical component pages 还没真正建立好
- 设计团队还在 Figma 里讨论 public API

### 7. 推荐的长期 operating model

更稳的长期模型是：

1. `source_token_v5.json` 继续作为 token source of truth
2. Figma `Semantic` variables 继续作为默认 binding layer
3. dedicated component pages 成为 component source of truth
4. 历史 cleanup boards 保留为 governance references
5. canonical pages 稳定后再补 Code Connect
6. 只有对成熟 family 才引入 contract-driven regenerate

### 8. 推荐的下一阶段

治理之后最重要的下一阶段不是立刻生成代码，而是 page canonization。

建议顺序：

1. 继续 harden 目标组件页
2. 明确哪些页面是 canonical edit surfaces
3. 把 handoff rule 写清楚：
   - canonical component page = handoff surface
   - Phase 0 / Phase 1 = governance history
4. 然后再开启：
   - Figma to Code
   - AI to Code
   - AI to Figma

### 9. 简短结论

这套 DS 已经接近可运营状态，但关键转折还在前面：

- 从 cleanup boards
- 过渡到 canonical component pages

等这一步完成后，这个文件会更安全地支持四类 workflow：

- Figma to Code
- AI to Figma
- AI to Code
- Human designer with Figma
