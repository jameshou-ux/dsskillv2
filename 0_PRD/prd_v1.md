# Design Token 管理架构 PRD

**Single Source of Truth + Adaptive Token Pipeline**

作者：James Hou
版本：v1.3
状态：Active

---

# 1. 概述

本文档定义了产品设计系统中的 **Design Token 管理架构**。

目标是在 Git 中建立一个 **Single Source of Truth（SSOT）** 的 Design Token 源文件，并通过自动化流程生成适配不同环境的 Token 格式，包括：

* Figma
* Runtime（Web / CSS / Tailwind / App）
* AI Native 系统

该架构确保：

* 所有设计决策来自统一 Token Source
* 设计与代码保持一致
* AI 能够理解并生成符合 Design System 的 UI

---

# 2. 核心原则

## 2.1 Single Source of Truth

所有 Design Token 存储在 Git 中的唯一源文件：

```
source/tokens.json
```

该文件是 **唯一允许手动编辑 Token 的地方**。

其他 Token 文件均为 **自动生成产物**。

---

## 2.2 单向同步

Token 只允许单向流动：

```
Git Source
    ↓
Token Compiler
    ↓
Adapters
    ↓
Consumers
```

消费者包括：

* Figma
* Runtime
* AI 系统

Figma **不是 Token Source**。

---

## 2.3 Adapter 架构

不同系统需要不同 Token 格式，因此通过 Adapter 生成：

```
figma.tokens.json
runtime.tokens.json
ai.tokens.json
```

---

# 3. Token 架构

Canonical Token Schema 使用四类 Token 视角：

```
primitive
semantic
pattern
component
```

这些类别用于把同一套设计值按不同上下文进行组织与聚类，而不是把它们理解为绝对、单向、严格串行的“楼层”。

其中：

* `primitive` 表示值从“基础视觉 scale”视角被聚类
* `semantic` 表示值从“界面角色语义”视角被聚类
* `pattern` 表示值从“可复用结构模式”视角被聚类
* `component` 表示值从“具体组件实现”视角被聚类
* `pattern` 与 `component` 是**并列关系**，不是强制串行依赖
* `pattern` 与 `component` 都优先引用 `semantic.*`
* `pattern` 与 `component` 在尺寸、圆角、间距、阴影等结构数值上可直接引用 `primitive.*`

---

## 3.1 Primitive Tokens

Primitive Token 表示基础视觉数值。

例如：

```
primitive.color.blue.500
primitive.spacing.8
primitive.radius.md
primitive.shadow.sm
```

特点：

* 表示视觉 scale
* 不包含 UI 语义
* 可复用
* 也是一种聚类视角，而不是“永远不被直接使用的底层”

---

## 3.2 Semantic Tokens

Semantic Token 表示设计语义。

例如：

```
semantic.text.primary
semantic.background.card
semantic.border.default
semantic.icon.primary
```

Semantic Token 通常引用 Primitive Token。

例如：

```
semantic.text.primary → primitive.color.navy.900
```

---

## 3.3 Pattern Tokens

Pattern Token 表示可复用的 UI 结构模式（Pattern / Composition）。

例如：

```
pattern.surface.card
pattern.surface.modal
pattern.layout.container
```

Pattern 关注的是“内容如何组织”和“一类界面如何重复出现”，而不是某个具体组件本身。

例如：

* `pattern.surface.card` 可被多个不同 card 组件复用
* `pattern.modal.confirmation` 可表达“标题 + 描述 + 明细区 + 操作区”的结构
* 同一种 pattern 可被不同容器承载，例如 `modal`、`drawer`、`side panel`

---

## 3.4 Component Tokens

Component Token 表示组件级设计规则。

例如：

```
component.button.primary.background
component.button.primary.padding
component.button.primary.radius
component.card.shadow
```

这些 Token 允许 Runtime 与 AI 系统重建组件。

Component 关注的是具体组件实例本身，而不是跨组件共享的结构模式。

`component layer` 的核心意义，不是再造一层新的视觉语义，而是把已有的 `semantic` / `primitive` 明确绑定到**具体组件的具体属性、变体、状态**上，使其能被设计系统、代码主题对象、组件实例和 AI 生成流程直接消费。

因此，`semantic` 与 `component` 的主要区别不在于“有没有视觉信息”，而在于**是否已经完成组件绑定**：

* `semantic` 回答“这是什么界面角色”，例如主文字、卡片背景、默认边框
* `component` 回答“这个组件在这个 variant / state 下具体该用什么”，例如 `button.primary.hover.background`

例如：

* `component.modal.*` 定义弹窗壳子的遮罩、背景、圆角、padding、close icon
* `component.button.*` 定义按钮在不同 variant / state 下的最终消费属性

Pattern 与 Component 的取舍原则：

* 复用“组件外壳和交互契约”时，使用 `component`
* 复用“内容布局和信息编排”时，使用 `pattern`
* 同一实际界面可以同时消费两者，例如 `modal` 的壳子由 `component.modal.*` 定义，内部布局由 `pattern.modal.*` 定义

---

# 4. Design Token System Architecture

本章节描述 **Design Token 系统整体架构**，展示 Token 从 Source 到各系统消费端的完整流程。

---

## 4.1 高层系统架构

```
                 ┌─────────────────────┐
                 │   Design Token      │
                 │   Source of Truth   │
                 │                     │
                 │   source/tokens.json│
                 │   (Git Repository)  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Token Compiler   │
                 │                     │
                 │  - Resolve tokens  │
                 │  - Validate schema │
                 │  - Expand alias    │
                 │  - Build adapters  │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼

         Figma Adapter   Runtime Adapter   AI Adapter

              │             │               │
              ▼             ▼               ▼

      figma.tokens.json  runtime.tokens.json  ai.tokens.json

              │             │               │
              ▼             ▼               ▼

       Figma Variables     CSS / Tailwind     AI UI Generation
       Tokens Studio       React / App        AI Reasoning
```

---

## 4.2 架构组件说明

### Token Source

Token Source 是整个系统的 **唯一设计数据源**。

```
source/tokens.json
```

特点：

* 存储在 Git
* 所有 Token 修改必须通过 PR
* 不依赖任何工具

---

### Token Compiler

Token Compiler 负责：

* 解析 Token 引用
* 校验 Schema
* 构建 Token 层级
* 生成适配不同系统的 Token

核心流程：

```
load tokens
   ↓
resolve references
   ↓
validate schema
   ↓
generate adapters
```

---

### Adapter Layer

Adapter Layer 负责生成不同系统需要的 Token。

#### Figma Adapter

生成：

```
adapters/figma/figma_tokens_adaptive.json   ← Tokens Studio 导入格式
adapters/figma/figma_variables_api.json     ← Figma REST API 格式（Enterprise）
```

通过 **Token importer by imToken** Figma Plugin 导入，生成带 Light / Dark 双 Mode 的 Figma Variables，无需付费计划。

---

#### Runtime Adapter

生成：

```
runtime.tokens.json
```

用于：

* CSS Variables
* Tailwind
* React
* Mobile

---

#### AI Adapter

生成：

```
ai.tokens.json
```

用于：

* AI UI generation
* AI reasoning
* AI design validation

---

# 5. Repository 结构

推荐结构：

```
design-tokens
│
├── source
│   └── tokens.json
│
├── adapters
│   ├── figma
│   │   └── tokens.figmatokens.json
│   │
│   ├── runtime
│   │   └── tokens.runtime.json
│   │
│   └── ai
│       └── tokens.ai.json
│
├── schema
│   ├── dtcg.schema.json
│   ├── figma.schema.json
│   ├── runtime.schema.json
│   └── runtime.schema.json
│
└── scripts
    └── build-tokens.ts
```

---

# 6. Token Schema 设计

Source Token Schema 需要兼容：

* Figma Native Variables
* Tokens Studio
* Runtime Token
* W3C DTCG
* AI Native Token

Schema 以 **Reference 文档形式独立维护**。

Token Compiler 会根据 schema 自动生成 Token。

---

# 7. Figma 集成

Figma Token 通过 Adapter 自动生成。

流程：

```
Git tokens
      ↓
generate figma.tokens.json
      ↓
Tokens Studio import
      ↓
Apply to Figma Variables
```

规则：

* Figma Token **只读**
* 不允许在 Figma 修改 Token
* Token 只允许 **从 Git 同步**

---

# 8. Runtime 集成

Runtime Token 用于：

* CSS Variables
* Tailwind
* React Theme
* Mobile Design Token

示例：

```
--color-text-primary
--spacing-sm
--radius-md
```

---

# 9. AI Native Token Layer

AI Adapter 生成：

```
ai.tokens.json
```

AI 可以通过这些 Token：

* 理解 UI
* 生成组件
* 保持设计一致性

---

# 10. Token Flow 示例

```
primitive.color.blue.500
        ↓
semantic.text.primary
        ↓
component.button.primary.background
```

消费者：

```
Figma
Runtime
AI
```

---

# 11. Design Governance

Token 修改流程：

```
token change
     ↓
pull request
     ↓
design review
     ↓
merge
     ↓
token rebuild
```

保证：

* 设计治理
* 版本可追溯

---

# 12. AI Token Consumption Model

AI 在生成 UI 时 **不直接生成视觉数值**。

AI 必须引用 Token。

例如：

```
background: semantic.background.primary
padding: primitive.spacing.8
radius: primitive.radius.md
```

而不是：

```
background: #007FFF
padding: 8px
```

---

# 13. AI UI Generation Flow

AI UI 生成流程：

```
User prompt
     ↓
AI reasoning
     ↓
Token lookup
     ↓
Component resolution
     ↓
Generate UI
```

---

# 14. AI Component Reconstruction

AI 可以通过 Token 层级重建组件：

```
component.button.primary
```

AI 可以解析：

```
layout
background
typography
spacing
```

---

# 15. AI Design Consistency

AI 生成 UI 必须遵守：

1. 不生成未定义设计值
2. 不直接写 hex color
3. spacing 必须来自 token scale

错误：

```
padding: 7px
```

正确：

```
padding: primitive.spacing.8
```

---

# 16. AI Token Pipeline

```
source tokens
      ↓
token compiler
      ↓
ai.tokens.json
      ↓
AI system
      ↓
UI generation
```

---

# 17. Token Naming Convention

Token 命名结构：

```
layer.category.element.variant.property
```

示例：

```
primitive.color.blue.500
semantic.text.primary
pattern.surface.card
component.button.primary.background
```

说明：

* `primitive` / `semantic` / `pattern` / `component` 使用不同命名语义，不要求所有层级深度完全相同
* 这四类命名首先是为了表达不同上下文下的聚类方式，而不是为了构造严格线性的依赖楼层
* `pattern` 与 `component` 都是对 `semantic` 的上层消费，但不应被理解为固定的前后串行关系

---

---

# 19. Figma Adaptive Token 输出规则

本章节定义 **Figma Adaptive Token JSON** 的严格输出格式规则。

---

## 19.1 文件结构

`figma_tokens_adaptive.json` 必须严格遵守以下结构：

```
{
  "Primitive": {
    "primitive": {
      "color": { ... }   ← 原始视觉值，无 alias
    }
  },
  "Light": {
    "semantic": { ... },  ← 仅包含 alias，引用 {primitive.color.*}
    "component": { ... }  ← 仅包含 alias，引用 {semantic.*} 或 {primitive.*}
  },
  "Dark": {
    "semantic": { ... },  ← 仅包含 alias，引用 {primitive.color.*}
    "component": { ... }  ← 路径与 Light.component 完全一致
  },
  "$themes": [...],
  "$metadata": { "tokenSetOrder": ["Primitive", "Light", "Dark"] }
}
```

---

## 19.2 Primitive Token 规则

* `$type` 必须为 `color`（或 `string` / `number` / `boolean` / `gradient`）
* `$value` 必须为直接视觉值（hex / rgba），`gradient` 除外
* **禁止** 在 Primitive 层使用 alias 引用
* 命名路径格式：`primitive.color.<palette>.<scale>`
  * 示例：`primitive.color.gray.50`、`primitive.color.navy.900_a40`

---

## 19.3 Semantic Token 规则（Light & Dark）

* Light 和 Dark 的 **token 路径必须完全一一对应**
* 每个 semantic token 必须：
  * 包含 `$type`
  * 包含 `$value`
  * 包含 `$description`（AI Native 语义描述，不得为空）
* **禁止** 在 semantic 层使用硬编码色值（除 gradient 外）
* **普通 Alias 格式**：`{primitive.color.<palette>.<scale>}`
  * 正确：`{primitive.color.navy.900}`
  * 错误：`{Primitive.color.navy.900}` / `#111D4A`
* **Gradient 格式**：当 `$type` 为 `gradient` 时，`$value` 必须是包含 `type`、`angle` 和 `stops` 数组的对象。`stops` 数组中的 `color` 必须使用 `{primitive.color.*}` alias。

---

## 19.4 Multi Mode 规则

* `$themes` 必须定义 `Light` 和 `Dark` 两个 theme
* Light theme：启用 `Primitive` + `Light`，禁用 `Dark`
* Dark theme：启用 `Primitive` + `Dark`，禁用 `Light`
* Token set 顺序：`["Primitive", "Light", "Dark"]`
* 扩展新 Mode（如 `HighContrast`）时，必须与 Light / Dark 保持相同的 semantic token 路径集合
* `component` token 在所有 Mode 下也必须保持相同路径集合（与 semantic 一样一一对应）

---

## 19.5 Figma Plugin 导入规则

* 使用 **Token importer by imToken** Figma Plugin 导入
* Plugin 使用 `figma.variables` API（无需 Enterprise 或付费计划）结合 `figma.createPaintStyle()`
* 导入行为：
  * `Primitive`：生成为 **Figma Variables**（包含 `Light` + `Dark` 两个 mode，两者的实际 primitive 值输入完全相同，这是由于 Figma 原生 Paint Style 目前不支持自身响应模式的主题切换，必须依赖底层 Variable 的双模属性。）。并且被设置为 `hiddenFromPublishing = true` 和 `scopes = []`，完全在设计师选色面板中隐藏。
  * `Semantic`（非 gradient）：生成为 **Figma Variables**（Light + Dark 两个 mode）。
  * `Semantic`（gradient）：生成为 **Figma Paint Styles**（分 `Light/` 和 `Dark/` 目录结构），因为 Figma Variables 原生暂不支持渐变。
  * `Component`（非 gradient）：生成为 **Figma Variables**（Light + Dark 两个 mode），命名路径保留 `component.*` 前缀，用于组件实例属性绑定与 AI 可读结构。
  * `Component`（gradient）：生成为 **Figma Paint Styles**（分 `Light/` 和 `Dark/` 目录结构），规则与 Semantic gradient 一致。
* 每次导入会完整清除并重建旧 Variables 集合与 Semantic / Component Styles，支持安全重复执行

---

## 19.6 API vs Plugin 决策背景及 Figma Plan 限制

本架构选择使用 Figma Plugin（客户端执行）而非 REST API（服务端执行）作为同步终点的核心原因在于 Figma 的生态权限限制：

1. **Variables 的 API 限制**：Figma Variables 的完整读写（POST）权限仅 **Enterprise (企业版)** 独占。Organization 及以下版本无写入权限。
2. **Styles 的 API 限制 (硬伤)**：对于无法使用 Variable 表达的视觉属性（如 Gradient 渐变、Effect 阴影等，需输出为 Paint Styles），**Figma REST API 针对所有 Plan（包括 Enterprise）均不开放写入操作**。
3. **架构务实结论**：由于本系统的 Design Token 中包含渐变（Gradient）等必须映射为 Style 的核心属性，即使升级至 Enterprise Plan 也无法实现 100% 无人干预的跨服务端 CI/CD 自动化同步，最终依然必须依赖 Plugin API 在客户端环境（如执行 `figma.createPaintStyle()`）打通闭环。
4. **终极定论**：当前针对所有 Token 集合采用 **Org/Pro Plan + Token importer Plugin** 的策略，是权衡灵活性与工具墙现状下，性价比最高、且唯一能完整覆盖 "Variables + Styles" 的自动化设计方案。

---

# 20. Source Token 保留规则

`source/tokens.json` 是系统的 **Single Source of Truth**，任何时候都必须完整保留以下特性。

---

## 20.1 必须保留的完整结构

| 结构 | 说明 |
|---|---|
| 多层结构（Multi-layer） | Primitive / Semantic / 上层消费结构（Pattern / Component）定义完整存在 |
| Light / Dark 双主题 | 两套 semantic token，路径完全对应 |
| Component Layer 完整性 | Light / Dark 中必须同时包含 component token，且路径完全对应 |
| AI Semantic 描述 | 每个 semantic token 的 `$description` 字段不得删除 |
| `$themes` 定义 | Light / Dark theme 配置完整保留 |
| `$metadata.tokenSetOrder` | token set 顺序字段完整保留 |
| AI native 语义命名 | 命名遵循 `category.role.state` 语义格式 |

---

## 20.2 禁止操作

* **禁止** 将 source token 的 semantic 层替换为硬编码值
* **禁止** 删除 `$description` 字段
* **禁止** 合并 Light 和 Dark 为单一 token set
* **禁止** 删除 `$themes` 或 `$metadata` 字段
* **禁止** 在 Primitive 层写入 alias
* **禁止** 删除 component 层或将 component 层扁平化为非结构化字段
* **禁止** 在已采用 pattern 的情况下将其退化为无结构字段集合

---

## 20.3 Source 与 Adapter 关系

```
source/tokens.json
    ↓ 编译 / 转换
adapters/figma/figma_tokens_adaptive.json   ← 仅变更 path 分隔符等格式
adapters/figma/figma_variables_api.json     ← RGB 归一化 + REST API 结构
```

Source 是 **语义层**，Adapter 是 **格式层**。两者都不得丢失信息。

---

# 21. Token 优化规则

当对现有 token JSON 进行优化、审计、重构时，必须严格遵守以下规则。

---

## 21.1 优化原则

* **保形优化（Structure-preserving）**：优化只改变 token 的值或描述，不得改变 token 的路径结构
* **不得无故删除 token**：即使 token 值在 Light / Dark 中相同，也必须在两套中分别定义
* **缺失值允许补充，不允许假设**：如某 token 在源文件中不存在，可补充；但不得为不存在的 token 填入推测值

---

## 21.2 优化允许的操作

| 操作 | 条件 |
|---|---|
| 修改 `$value` | 必须仍为 `{primitive.*}` alias，不得改为硬编码 |
| 修改 `$description` | 必须保留 AI 语义属性，描述更准确即可 |
| 新增 token | 路径必须符合 `semantic.category.role` 格式 |
| 修改 Primitive 值 | 允许，但不得影响现有 alias 引用 |
| 补充缺失的 `$description` | 必须写 AI native 语义描述 |
| 新增 pattern token | 路径必须符合 `pattern.<patternGroup>.<patternName>.<property>` 或等价结构化格式 |
| 修改 pattern `$value` | 必须仍为 alias（`{semantic.*}` 优先，结构数值可用 `{primitive.*}`） |
| 新增 component token | 路径必须符合 `component.<component>.<variant>.<state>.<property>` |
| 修改 component `$value` | 必须仍为 alias（`{semantic.*}` 优先，或 `{primitive.*}`） |

---

## 21.3 优化禁止的操作

* **禁止** 修改 token 路径（除非明确重命名需求并同步所有引用）
* **禁止** 将 alias 替换为硬编码值（即使两者当前等价）
* **禁止** 删除某 Light token 而在 Dark 中保留同路径 token
* **禁止** 将 semantic 层直接指向另一个 semantic token（跨层引用）
* **禁止** 在没有对应 Primitive token 的情况下在 semantic 中使用该 alias
* **禁止** 在 pattern 层写入硬编码视觉值（如 `#xxxxxx`、`12px`）
* **禁止** pattern 层直接引用另一个 pattern token（避免链式依赖）
* **禁止** 在 component 层写入硬编码视觉值（如 `#xxxxxx`、`12px`）
* **禁止** component 层直接引用另一个 component token（避免链式依赖）
* **禁止** Light / Dark 的 component 路径不一致

---

## 21.4 缺失值处理规则

如发现 token 值确实缺失（如源文件中某 token 根本不存在）：

1. 记录为 `missing`，不得填入随机值
2. 优化报告中标记为 `[MISSING]`
3. 由设计师确认后再补充
4. 补充时必须同时在 `Light` 和 `Dark` 中定义

---

# 22. Pattern / Component 上层消费规范

本章节定义 `pattern` 与 `component` 的可执行规则，确保 token 优化与重构后仍可被 Source、Figma、Runtime 一致消费。

---

## 22.1 目标与定位

`pattern` 与 `component` 都是对同一套 design token 在不同上下文下的再组织方式，但两者解决的问题不同。

定位规则：

* `primitive`：保存原始视觉 scale 这一聚类视角
* `semantic`：保存跨组件语义这一聚类视角
* `pattern`：保存跨组件、跨容器可复用的结构模式与内容编排方式
* `component`：保存组件实例化决策（最终供 UI 直接消费）
* `pattern` 与 `component` 是**并列关系**，不是强制的线性“上一层 / 下一层”
* 四者更适合被理解为“同一设计值在不同上下文中的聚类方式”，而不是绝对的楼层关系

关系应理解为：

```
             semantic
            /        \
     pattern          component
            \        /
            primitive
```

说明：

* 上图表达的是“常见引用关系与聚类重心”，不是唯一合法依赖路径
* 同一个值可以在不同上下文下被不同类别引用和复用
* 哪怕是 `primitive`，本质上也是一种按基础视觉 scale 组织值的聚类方式

补充原则：

* 颜色、文本、边框、背景等视觉角色，优先引用 `semantic.*`
* 间距、圆角、尺寸、阴影等基础尺度，可直接引用 `primitive.*`
* 不应假设 `component` 必然建立在 `pattern` 之上；两者可独立存在，也可同时服务于同一实际界面
* 不应假设 `primitive` 只能作为“最底层被动来源”；在尺寸与比例体系中，它也可以被直接消费

### 22.1.1 Pattern 的适用场景

适合使用 `pattern` 的情况：

* 需要抽象一类可复用的内容结构或布局模式
* 多个不同组件共享相同的信息组织方式
* 同一种内容模式可能承载在不同容器中，例如 `modal` / `drawer` / `side panel`

示例：

```
pattern.surface.card.background = {semantic.background.card}
pattern.surface.card.title = {semantic.text.primary}
pattern.surface.card.body = {semantic.text.secondary}
pattern.modal.confirmation.sectionBackground = {semantic.background.modal_section}
pattern.modal.confirmation.detailText = {semantic.text.secondary}
```

### 22.1.2 Component 的适用场景

适合使用 `component` 的情况：

* 需要定义某个具体组件的外壳、状态、variant 与最终消费属性
* 该 token 直接服务于代码实现、组件库绑定、Runtime 主题对象
* 需要把通用 `semantic` 角色绑定为组件级 API，例如把 `semantic.background.modal` 绑定为 `component.modal.default.default.background`

换句话说，`component layer` 的主要意义在于“绑定”：

* 直接使用 `semantic` 时，你表达的是通用视觉角色
* 使用 `component` 时，你表达的是组件实现契约
* `component` 把本来抽象的语义 token，映射为组件库、主题对象、Figma Variables、AI 生成器都能稳定消费的字段路径

判断上可以这样理解：

* 如果你只是在说明“这里应该是主文字 / 卡片背景 / 弹窗背景”，那仍是 `semantic`
* 如果你已经在说明“Modal 的 header background / Button primary 的 hover background / Input disabled border”，那就应该进入 `component`

示例：

```
component.modal.default.default.background = {semantic.background.modal}
component.modal.default.default.backdrop = {semantic.background.backdrop}
component.modal.default.default.radius = {primitive.radius.lg}
component.button.primary.default.background = {semantic.fill.secondary}
```

### 22.1.3 Pattern / Component 取舍规则

判断标准：

* 复用“组件外壳和交互契约”时，使用 `component`
* 复用“内容布局和信息编排”时，使用 `pattern`
* 如果一个界面只有轻微文案差异，而没有稳定复用的结构差异，则只建 `component`，不要过度抽象 `pattern`
* 如果一个界面既有稳定的容器外壳，又有可重复出现的内部结构，则同时使用 `component` 与 `pattern`

以 `modal` 为例：

* `component.modal.*` 定义遮罩、容器背景、圆角、header/footer padding、close icon 等“弹窗壳子”
* `pattern.modal.confirmation.*` 定义“标题 + 描述 + 明细区 + 操作区”的内部组织方式

因此，`modal` 是同时使用两者的典型场景。

---

## 22.2 Source Token（`source/tokens.json`）规范

### 22.2.1 文件结构要求

`source/tokens.json` 中，`Light` 与 `Dark` 必须同时包含 `semantic` 与 `component`；若引入 `pattern`，也必须在两套 theme 中保持路径集合一致：

```
{
  "Primitive": {
    "primitive": { ... }
  },
  "Light": {
    "semantic": { ... },
    "pattern": { ... },
    "component": { ... }
  },
  "Dark": {
    "semantic": { ... },
    "pattern": { ... },
    "component": { ... }
  }
}
```

### 22.2.2 命名层级要求

`pattern` 推荐使用：

```
pattern.<patternGroup>.<patternName>.<property>
```

约束：

* `<patternGroup>`：模式组（如 `surface` / `layout` / `modal`）
* `<patternName>`：模式名（如 `card` / `confirmation` / `tokenSummary`）
* `<property>`：模式暴露的消费属性（如 `background` / `title` / `body` / `sectionBackground`）

`component` 路径统一使用：

```
component.<component>.<variant>.<state>.<property>
```

约束：

* `<component>`：组件名（如 `button` / `input` / `card`）
* `<variant>`：变体（如 `primary` / `secondary` / `danger`）
* `<state>`：状态（如 `default` / `hover` / `pressed` / `disabled`）
* `<property>`：最终消费属性（如 `background` / `text` / `border` / `paddingX` / `radius`）

### 22.2.3 值与引用规则

* `pattern` 层 **必须使用 alias**
* `component` 层 **必须使用 alias**
* `pattern` / `component` 均应优先引用 `semantic.*`
* 间距、圆角、尺寸、阴影等结构数值可引用 `primitive.*`
* **禁止** 直接写硬编码值
* **禁止** `pattern -> pattern` 链式引用
* **禁止** `component -> component` 链式引用

示例（正确）：

```
pattern.modal.confirmation.sectionBackground = {semantic.background.modal_section}
pattern.modal.confirmation.detailPadding = {primitive.spacing.16}
component.button.primary.default.background = {semantic.background.brand}
component.button.primary.default.text = {semantic.text.onBrand}
component.button.primary.default.paddingX = {primitive.spacing.12}
component.button.primary.default.radius = {primitive.radius.md}
```

### 22.2.4 Theme 对齐规则

* `Light.pattern` 与 `Dark.pattern` 的路径必须完全一致
* `Light.component` 与 `Dark.component` 的路径必须完全一致
* 若某路径在一个 mode 存在，另一个 mode 必须存在同路径 token
* `pattern` 与 `component` 均允许两边 alias 最终解析到不同 semantic token，以表达主题差异

---

## 22.3 Figma Adaptive Token（`figma_tokens_adaptive.json`）规范

### 22.3.1 输出结构

Figma 输出必须保留 `component`；若 Source 中定义了 `pattern`，输出也必须保留 `pattern`：

```
{
  "Primitive": { "primitive": { ... } },
  "Light": {
    "semantic": { ... },
    "pattern": { ... },
    "component": { ... }
  },
  "Dark": {
    "semantic": { ... },
    "pattern": { ... },
    "component": { ... }
  }
}
```

### 22.3.2 导入与映射规则

* `pattern` 非 gradient token 导入为 Figma Variables
* `pattern` gradient token 导入为 Paint Styles（`Light/`、`Dark/` 目录）
* `component` 非 gradient token 导入为 Figma Variables
* `component` gradient token 导入为 Paint Styles（`Light/`、`Dark/` 目录）
* Figma 中变量名需保持与 Source 路径一致（只允许格式层转换，不允许语义变更）
* `pattern` / `component` token 不得在 Figma 侧被手动改写为新值

---

## 22.4 Runtime Token（`runtime`）规范

Runtime 层必须输出可直接消费的 component token，至少覆盖以下文件之一：

```
adapters/runtime/tokens.runtime.json
```

当需要按平台拆分时，允许额外输出：

```
adapters/runtime/tokens.css.json
adapters/runtime/tokens.tailwind.json
adapters/runtime/tokens.react.json
adapters/runtime/tokens.mobile.json
```

### 22.4.1 Runtime Canonical JSON 要求

`tokens.runtime.json` 至少包含：

```
{
  "semantic": { ... },
  "pattern": { ... },
  "component": { ... }
}
```

约束：

* 若 runtime 选择输出 `pattern`，其路径必须与 Source 的目标主题路径一致
* `component` 路径必须与 Source 的 `Light` 或目标主题路径一致
* 允许输出 resolved 值（如 hex、px）供运行时性能优化
* 但必须保留 `sourceRef`（原 token 路径）用于追溯

示例：

```
{
  "component": {
    "button": {
      "primary": {
        "default": {
          "background": { "value": "#246BFD", "sourceRef": "component.button.primary.default.background" },
          "text": { "value": "#FFFFFF", "sourceRef": "component.button.primary.default.text" }
        }
      }
    }
  }
}
```

### 22.4.2 各 Runtime 文件映射要求

* CSS：生成 `--component-button-primary-default-background` 这类变量
* Tailwind：将 component token 注入 `theme.extend` 或插件映射
* React：在 Theme 对象中保留 `theme.component.button.primary.default.*` 路径
* Mobile：导出平台可消费结构（iOS/Android），但路径语义必须与 Source 一致

---

## 22.5 编译与校验规则（强制）

Token Compiler 对 `pattern` / `component` 层必须执行以下校验：

1. `component` 路径格式校验：必须符合 `component.<component>.<variant>.<state>.<property>`
2. `pattern` 路径格式校验：必须符合 `pattern.<patternGroup>.<patternName>.<property>` 或等价约定
3. 引用合法性校验：`pattern` / `component` 仅允许引用 `semantic.*` 或 `primitive.*`
4. Theme 完整性校验：Light / Dark component 路径集合必须完全一致；若存在 pattern，也必须完全一致
5. 类型校验：同路径在不同 mode 下 `$type` 必须一致
6. 追溯校验：Runtime resolved 输出必须可回溯到 `sourceRef`

任一校验失败，编译必须报错并阻断产物发布。

---

# 18. 总结

该架构建立了一套 **AI Native Design Token Infrastructure**。

核心特点：

* Git Single Source of Truth
* Adapter Token Pipeline
* Schema Reference Architecture
* AI Native Token Consumption
* Scalable Design System

Design Token 成为：

```
Design System
Runtime
AI UI Generation
```

之间的统一语义层。
