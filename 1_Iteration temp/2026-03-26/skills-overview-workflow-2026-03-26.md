# Figma DS Skills Overview, Layering, and Recommended Workflow

Date: 2026-03-26

Target Figma file:
`DBQdb8ymhIfTPS9GmcTqaR`

## 1. Skill Layering Summary

The Figma-related skills do not all play the same role. The cleanest way to reason about them is by layer.

### Layer A: execution foundation

- `figma-use`

This is the mandatory execution base for any serious Figma Plugin API read or write.

Without it:

- `use_figma` writes are not safely or correctly structured
- page switching, font loading, node ID return, atomic failure handling, and variable-binding gotchas are easy to get wrong

This is the only real hard dependency in the stack.

### Layer B: governance and orchestration

- `figma-generate-library`

This is the top-level DS workflow and sequencing layer.

It answers:

- what phase comes first
- when to do foundations vs components
- how to organize pages
- when to validate and checkpoint

It is not just a plan document, but it still depends on `figma-use` to actually execute.

### Layer C: specialized governance workflows

- `audit-design-system`
- `apply-design-system`
- `sync-figma-token`
- `rad-spacing`

These are not hard dependencies in the same way as `figma-use`, but they are high-value method packs for recurring governance tasks.

#### `audit-design-system`

Use for read-only diagnosis:

- where drift exists
- where components are local instead of canonical
- where tokens and styles are not actually bound

#### `apply-design-system`

Use for section-level or page-level DS reconnection:

- exact swap with library components
- rebuild from primitives
- multi-section normalization

This is useful, but not strictly required. Similar work can still be done manually with `figma-use` plus audit logic.

#### `sync-figma-token`

Use for token parity between code and Figma.

This is the right tool for:

- missing tokens
- alias mismatch
- scope mismatch
- code syntax mismatch

#### `rad-spacing`

Use when the problem is not component architecture but spacing hierarchy:

- gap
- padding
- nested grouping
- page-level layout rhythm

### Layer D: contract-driven generation

- `cc-figma-tokens`
- `cc-figma-component`

These are specialized generators, not general governance tools.

#### `cc-figma-tokens`

This assumes there is already a contract-side token source.

Its job is to:

- read the contract token files
- create or update `Primitives` and `Semantic`
- set scopes
- set code syntax
- build alias chains

It is best understood as a contract-driven token compiler into Figma variables.

#### `cc-figma-component`

This assumes:

- contract-side component definition exists
- Figma-side token collections already exist

Its job is to:

- read the component contract
- derive the variant matrix, props, slots, and bindings
- generate or regenerate a canonical component set

It is much closer to regenerate than to patch.

### Layer E: downstream and adjacent workflows

- `figma-code-connect-components`
- `figma-create-design-system-rules`
- `figma-create-new-file`
- `figma-generate-design`
- `edit-figma-design`
- `multi-agent`

These are important, but they are not part of the core DS cleanup loop.

#### `figma-code-connect-components`

Use after component APIs and canonical DS pages are stable.

#### `figma-create-design-system-rules`

Use to formalize project rules and the operating model around Figma and code.

#### `figma-create-new-file`

Use when a clean sandbox or branch file is needed.

#### `figma-generate-design`

Use to generate or update full screens from code or a product description, after the DS is stable enough to be reused.

#### `edit-figma-design`

Use for text-driven design creation or iteration, not token governance.

#### `multi-agent`

Use for parallel planning, read-side exploration, or implementation coordination. Do not use it for parallel `use_figma` writes.

## 2. How The Skills Relate To Each Other

### `figma-generate-library` vs `figma-use`

- `figma-generate-library` defines the build and governance logic
- `figma-use` is the execution substrate

Without `figma-use`, `figma-generate-library` cannot reliably perform actual Figma writes.

### `figma-generate-library` vs `apply-design-system`

- `figma-generate-library` is the broader DS framework
- `apply-design-system` is a more specific workflow for reconnecting an existing page or section to a DS

`apply-design-system` is optional but helpful. `figma-use` is not optional in the same way.

### `figma-generate-library` vs `cc-figma-tokens` / `cc-figma-component`

- `figma-generate-library` is the general DS build and governance framework
- `cc-figma-tokens` is a contract-driven token generation path
- `cc-figma-component` is a contract-driven component generation path

The `cc-*` skills are best understood as specialized implementations of parts of the broader DS workflow, not as replacements for it.

## 3. Recommended Default Workflow For This Repo

For the current DS file, the practical governance flow should be:

1. `figma-use`
   - inspect pages, variables, styles, components
2. `audit-design-system`
   - identify actual drift and missing bindings
3. `sync-figma-token`
   - run dry-run parity checks when code token alignment is in scope
4. `figma-use`
   - apply targeted fixes
5. `apply-design-system`
   - use only when the work is section-sized or page-sized
6. `rad-spacing`
   - normalize layout hierarchy if needed
7. `figma-use`
   - final precise cleanup and validation

## 4. Recommended Use Cases By Skill

### Use as core workflow

- `figma-use`
- `figma-generate-library`
- `audit-design-system`
- `sync-figma-token`

### Use when scope justifies it

- `apply-design-system`
- `rad-spacing`

### Use when contract infrastructure is ready

- `cc-figma-tokens`
- `cc-figma-component`

### Use after DS stabilization

- `figma-code-connect-components`

### Use for governance formalization or new workspaces

- `figma-create-design-system-rules`
- `figma-create-new-file`

### Use for new screen creation rather than DS cleanup

- `figma-generate-design`
- `edit-figma-design`

### Use for coordination, not canvas mutation

- `multi-agent`

## 5. Decision Rules

### If the task is Figma-side governance on an existing messy DS file

Use:

- `figma-generate-library`
- `figma-use`
- `audit-design-system`
- `sync-figma-token`
- optionally `apply-design-system`
- optionally `rad-spacing`

Do not default to `cc-*`.

### If the task is rebuilding tokens from a contract-side source

Use:

- `cc-figma-tokens`
- with `figma-use`
- within the sequencing logic of `figma-generate-library`

### If the task is generating or regenerating a component from contract

Use:

- `cc-figma-component`
- after `cc-figma-tokens`
- with `figma-use`
- and under the phase logic of `figma-generate-library`

### If the task is connecting mature Figma components to code

Use:

- `figma-code-connect-components`

### If the task is creating a new screen or concept

Use:

- `figma-generate-design`
- or `edit-figma-design`

## 6. What Was Actually Used In The Recent Cleanup Phases

The recent cleanup phases primarily used:

- `figma-use`
- `figma-generate-library`
- `sync-figma-token`
- `audit-design-system`
- `rad-spacing`

Secondarily:

- `apply-design-system`

The `cc-*` skills were not the main mechanism because the recent work was governance and migration, not contract-first generation.


---

## 中文翻译

### 1. Skill 分层总结

这些 Figma 相关 skill 不是同一层级的能力，最清晰的理解方式是按层拆开。

#### A 层：执行基础层

- `figma-use`

这是所有严肃 Figma Plugin API 读写的基础执行层。没有它，`use_figma` 写入很容易在页面切换、字体加载、节点 ID 返回、原子失败处理、变量绑定等方面出错。它是整个栈里唯一真正的硬依赖。

#### B 层：治理与编排层

- `figma-generate-library`

这是设计系统的总 workflow 和 phase 编排层。它负责定义：

- 先做什么、后做什么
- foundations 和 components 的先后关系
- 页面结构如何组织
- 每一阶段何时验证、何时 checkpoint

它不是纯计划文档，但它本身仍然依赖 `figma-use` 才能真正执行。

#### C 层：专项治理层

- `audit-design-system`
- `apply-design-system`
- `sync-figma-token`
- `rad-spacing`

这些不是像 `figma-use` 那样的硬依赖，但都是高价值的方法包。

- `audit-design-system`：做只读诊断，查 drift、查本地 wrapper、查未绑定 token/style。
- `apply-design-system`：做页面或 section 级的 DS 重连，适合 exact swap、primitive 组合重建、多 section 规范化。
- `sync-figma-token`：做 code token 与 Figma variable 的一致性检查。
- `rad-spacing`：做 gap、padding、层级间距的结构性规范化。

#### D 层：contract 驱动生成层

- `cc-figma-tokens`
- `cc-figma-component`

这两个不是通用治理工具，而是基于 contract 的专用生成器。

- `cc-figma-tokens`：读取 contract 侧 token 文件，生成或更新 Figma 里的 `Primitives` / `Semantic`，并补齐 scope、code syntax、alias 链。
- `cc-figma-component`：读取 component contract，推导 variant、props、slots、bindings，并生成或重生成一个 canonical component set。

它们更接近“编译 / regenerate”，而不是“人工 patch”。

#### E 层：下游与相邻工作流层

- `figma-code-connect-components`
- `figma-create-design-system-rules`
- `figma-create-new-file`
- `figma-generate-design`
- `edit-figma-design`
- `multi-agent`

这些都重要，但不属于核心 DS cleanup loop：

- `figma-code-connect-components`：组件页稳定后再接 code
- `figma-create-design-system-rules`：沉淀项目规则
- `figma-create-new-file`：新建 sandbox 或 branch 文件
- `figma-generate-design`：从代码或描述生成 screen
- `edit-figma-design`：文本驱动的设计迭代
- `multi-agent`：做并行分析或协作，不用于并行 Figma 写入

### 2. 几个关键 skill 的关系

#### `figma-generate-library` vs `figma-use`

- `figma-generate-library` 负责方法论和 phase
- `figma-use` 负责真正的执行

没有 `figma-use`，`figma-generate-library` 不能可靠地完成 Figma 写入。

#### `figma-generate-library` vs `apply-design-system`

- `figma-generate-library` 是更上位的 DS 框架
- `apply-design-system` 是把已有页面或 section 接回设计系统的专用 workflow

`apply-design-system` 没有也能做类似工作，但效率和方法论会差一些；`figma-use` 则不同，它是底座。

#### `figma-generate-library` vs `cc-*`

- `figma-generate-library` 是通用 DS build / governance 框架
- `cc-figma-tokens` 是 contract 驱动的 token 生成路径
- `cc-figma-component` 是 contract 驱动的 component 生成路径

`cc-*` 最好理解为 broader DS workflow 的专门实现，而不是对它的替代。

### 3. 当前 repo 的推荐默认流程

对于当前这个 DS 文件，更合适的治理流是：

1. `figma-use` 盘点页面、变量、样式、组件
2. `audit-design-system` 找 drift 和缺失绑定
3. `sync-figma-token` 在涉及 code token 对齐时做 dry-run
4. `figma-use` 做有针对性的修复
5. `apply-design-system` 在 scope 达到页面或 section 级时使用
6. `rad-spacing` 处理布局层级问题
7. `figma-use` 做最后的精修和验证

### 4. 按使用场景划分

#### 核心 workflow

- `figma-use`
- `figma-generate-library`
- `audit-design-system`
- `sync-figma-token`

#### 视 scope 使用

- `apply-design-system`
- `rad-spacing`

#### contract 基础设施成熟后使用

- `cc-figma-tokens`
- `cc-figma-component`

#### DS 稳定后再使用

- `figma-code-connect-components`

#### 规则沉淀或新文件场景使用

- `figma-create-design-system-rules`
- `figma-create-new-file`

#### 新 screen / 新概念设计场景使用

- `figma-generate-design`
- `edit-figma-design`

#### 协作与并行分析使用

- `multi-agent`

### 5. 决策规则

- 如果任务是治理一个已有且 messy 的 DS 文件，优先走治理流，不要默认走 `cc-*`。
- 如果任务是从 contract token 源重建变量层，再用 `cc-figma-tokens`。
- 如果任务是从 component contract 生成或重生成组件，再用 `cc-figma-component`。
- 如果任务是把成熟组件接到代码，使用 `figma-code-connect-components`。
- 如果任务是生成新页面或新 screen，使用 `figma-generate-design` 或 `edit-figma-design`。

### 6. 最近清理阶段实际主要用到的 skill

主要使用了：

- `figma-use`
- `figma-generate-library`
- `sync-figma-token`
- `audit-design-system`
- `rad-spacing`

次要使用了：

- `apply-design-system`

`cc-*` 不是这轮的主机制，因为这轮做的是治理和迁移，不是 contract-first 生成。
