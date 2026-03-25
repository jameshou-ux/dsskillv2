# 过去 2 天 Repo 工作时间线整理

日期：2026-03-23  
范围：基于过去 2 天在 repo 内可见的提交、当前工作区 diff、迭代产物和 adapter / plugin 变更整理  
用途：用于内部复盘、汇报、handoff

## 一句话结论

这 2 天的工作主线，不是单点补 token，而是在持续收敛 3 个核心矛盾：

- `source 语义完整性` vs `Figma 实际可用性`
- `命名清晰度` vs `下游兼容成本`
- `设计真实度` vs `工程可绑定性`

整体演进方向很明确：

- 先清 repo 结构
- 再补颜色和状态系统
- 再把 typography 升级成一等 token
- 最后把 `source truth` 和 `Figma consumption` 明确拆开

## 时间线

### 2026-03-22 21:10
阶段：文件整理基线

#### 当时的关键矛盾

repo 里过程文件、旧展示文件、历史产物比较散，继续推进 token 系统时，会越来越难回答一个基本问题：`当前到底哪个文件才是准的`。

#### 挑战点

- 不能让“整理仓库”本身拖慢设计系统迭代
- 但如果不先整理，后续每一轮版本演进都会越来越难追踪

#### 做法

通过提交 `2cb7296` 先做一轮 `regular file organization`，把历史文件和当前工作面拆开。

#### 解法本质

先把工作台面收干净，再继续做 schema 和 adapter 迭代。

#### Tradeoff

- 好处：后续版本演进更清晰
- 代价：部分上下文不再摆在主路径上，后面回溯更依赖 commit 和文件命名

---

### 2026-03-22 21:32
阶段：先做整体展示面

#### 当时的关键矛盾

需要快速看到“整个系统长什么样”，但 source schema 还在变化中。

#### 挑战点

- 是先把 source 打磨稳定，再出展示页
- 还是先做一个可读的全局视图，反过来帮助判断 schema 问题

#### 做法

先基于 AI adapter 输出生成设计系统展示页：

- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/Iteration temp/design-system.html`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/design-system.html)

#### 解法本质

先把系统“看见”，让结构问题暴露出来，而不是只在 JSON 里推演。

#### Tradeoff

- 好处：反馈快，便于发现命名和分层问题
- 代价：这版展示依赖 downstream adapter，不是 source-first，一旦 source 变了就要整体重刷

---

### 2026-03-22 23:18 到 2026-03-23 01:01
阶段：`v3 -> v4`

#### 当时的关键矛盾

颜色系统既要保留设计稿里的表达力，又要变成工程上可稳定消费的 token 体系。

#### 挑战点

- alpha 和透明叠加很多，设计表达比较细
- 但工程侧需要更稳定的 primitive 和 semantic 结构
- 状态色体系也还不够完整

#### 做法

在 `v4` 中扩充了颜色系统和状态系统，重点包括：

- blue alpha steps
- 新的 green / red / orange 状态能力
- 更完整的 semantic 状态层

对应产物：

- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/Iteration temp/source_token_v4.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/source_token_v4.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/Iteration temp/design-system-v4.html`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/design-system-v4.html)

#### 解法本质

先把颜色和状态系统打厚，建立更完整的 `primitive -> semantic` 链路，为后续 typography 和 plugin 接入打基础。

#### Tradeoff

- 好处：覆盖面更全，语义更稳
- 代价：token 数量上升，adapter 类型推断和 alias 传递开始变复杂

---

### 2026-03-23 12:01
阶段：`v5`

#### 当时的关键矛盾

typography 之前更像“展示信息”或附属定义，但实际上已经需要变成可以贯穿 source、adapter、Figma plugin 的一等 token。

#### 挑战点

- 文本样式不能再只是文档里的例子
- 必须被正式建模
- 但一旦正式建模，所有下游都会一起被牵动

#### 做法

在提交 `9dff3e5` 中把 typography 升级为 first-class token：

- 从 Figma 节点 `33297:16462` 回填 typography 数据
- 引入 typography primitive
- 引入 semantic text-style token

对应产物：

- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/Iteration temp/source_token_v5.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/source_token_v5.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/Iteration temp/design-system-v5.html`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/design-system-v5.html)

#### 解法本质

把 typography 从“附属说明”升级成“正式 token layer”。

#### Tradeoff

- 好处：source 质量明显提升，文本语义真正进入设计系统
- 代价：AI、runtime、Figma plugin 全部都要跟着升级

---

### 2026-03-23 13:15 之后
阶段：`v5` 后的下游重建

#### 当时的关键矛盾

source 语义一旦升级，下游所有消费层都必须理解 typography，而且要尽量保留可追踪性。

#### 挑战点

- 需要同步 AI adapter、runtime adapter、Figma adapter
- 不能让 source 和 downstream 完全脱节
- 还要处理命名升级带来的兼容问题

#### 做法

重建了多组下游产物，包括：

- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/ai/ai.tokens.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/ai/ai.tokens.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/runtime/tokens.css.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/runtime/tokens.css.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/runtime/tokens.mobile.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/runtime/tokens.mobile.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/runtime/tokens.react.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/runtime/tokens.react.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/runtime/tokens.runtime.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/runtime/tokens.runtime.json)
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/runtime/tokens.tailwind.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/runtime/tokens.tailwind.json)

#### 解法本质

开始形成“一套 richer source，喂多个 consumer”的结构。

#### Tradeoff

- 好处：source 的中心地位更强
- 代价：命名进入过渡态，很多下游还保留 `semantic.textStyle.*` 旧路径，迁移没有完全收口

---

### 2026-03-23 20:51 到 22:08
阶段：当前 `v6 / figma_tokens_v2` 工作段

#### 当时的关键矛盾

source 需要保留完整语义结构，但 Figma import 的体验会因为层级太多、名字太长而迅速变差。

#### 挑战点

- 如何让 source 继续保留 `primitive / semantic / pattern / component`
- 同时又让 Figma 只暴露最有用、最适合绑定的部分

#### 做法

这一段当前工作区里能看到几个关键动作：

- 把 `semantic.textStyle` 重命名为 `semantic.font`
- 把 radius 从 `[MISSING]` 补成真实值：`4 / 10 / 16 / 9999`
- 新增 Figma-facing adapter：
  - [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/figma/figma_tokens_v2.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/figma/figma_tokens_v2.json)
- 更新 Figma plugin：
  - [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/figma-plugin/code.js`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/figma-plugin/code.js)
- 在 README 里明确写清 Figma consumption rules：
  - [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/figma-plugin/README.md`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/figma-plugin/README.md)
- 产出新的展示版本：
  - [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/Iteration temp/design-system-v6.html`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/Iteration%20temp/design-system-v6.html)

#### 解法本质

不是去压平 source，而是把“source truth”和“Figma consumption”明确拆开：

- source 保留完整语义层级
- Figma 只暴露 `primitive + semantic`
- `pattern + component` 不再作为 Figma import 主表面
- semantic font style 在 Figma 中进一步扁平化命名，提高 picker 可用性

#### Tradeoff

- 好处：Figma picker 更干净，绑定体验更实用
- 代价：Figma 中看到的结构不再等于 source 中的结构，使用者需要接受这套双层心智模型

## 版本脉络

- `design-system.html`
  - 早期从 AI adapter 出发的全局展示面
- `v3`
  - 早期 source 结构化版本
- `v4`
  - 颜色与状态系统扩充
- `v5`
  - typography 成为 first-class token
- `v6`
  - 面向 Figma 消费体验的重构，开始明确 source 与 import surface 的边界

## 这 2 天最核心的 3 个矛盾

### 1. Source 语义完整性 vs Figma 实际可用性

source 希望完整保留：

- primitive
- semantic
- pattern
- component

但 Figma import 如果完整照搬，变量和样式选择器会迅速变得难用。

当前解法：

- source 保持完整
- Figma-facing adapter 主动过滤和扁平化

对应 tradeoff：

- 语义没有丢
- 但 source 结构和 Figma 结构不再一一对应

### 2. 命名清晰度 vs 下游兼容成本

新命名如：

- `heroTitle`
- `bodyPrimary`
- `actionLabel`

明显比旧命名更清晰，但下游很多产物仍保留 `semantic.textStyle.*` 旧引用。

当前解法：

- 先把命名往前推
- 再接受一段双语义并存的过渡期

对应 tradeoff：

- 命名体系更强
- 但短期内 schema 迁移不完全收口

### 3. 设计真实度 vs 工程可绑定性

设计稿中很多值是：

- 透明叠加
- composited 结果
- 占位值
- 未完全确认的值

但工程侧要的是：

- 可绑定
- 可复用
- 可追踪
- 可在 Figma / runtime 中稳定工作

当前解法：

- 逐步把模糊值替换成明确值
- 典型例子就是 radius 从 `[MISSING]` 变成 `4 / 10 / 16 / 9999`

对应 tradeoff：

- 工程落地更稳定
- 但需要在 fidelity 和 simplification 之间持续做判断

## 当前仍未完全收口的点

- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/source/tokens.json`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/source/tokens.json) 还没有完全追平当前 `v5 -> v6` 的方向
- runtime 和 AI 侧仍有大量 `semantic.textStyle.*` 历史引用
- [`/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj/adapters/figma/build_figma_adapter_v2.py`](/Users/jameshou/Desktop/imToken%20Repos/dsskillv2%20proj/adapters/figma/build_figma_adapter_v2.py) 目前更像过滤层，不是长期稳定的独立生成链路

## 汇报时可以直接讲的结尾

如果用一句话总结，这 2 天做的不是简单“补 token”，而是在把这个 repo 从一个不断堆内容的 token 集合，往一套有明确边界的设计系统工程链路推进：

- source 负责语义完整
- adapters 负责面向不同消费端转译
- Figma import 只保留最有用的绑定面

所以这 2 天最大的成果，不只是版本从 `v3/v4/v5` 推到 `v6`，而是开始把 `source of truth` 和 `consumption surface` 真正分开了。
