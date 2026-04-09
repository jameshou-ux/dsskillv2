# Figma DS Page Structure, Current Completeness, and Next Recommendations

Date: 2026-03-26

Target Figma file:
`DBQdb8ymhIfTPS9GmcTqaR`

## 1. Current DS Page Structure

The file currently contains three kinds of DS pages:

1. foundations and token pages
2. historical cleanup and governance pages
3. emerging canonical component pages

## 2. Main Pages And Their Roles

### `1297:17025` — `Design token`

Role:

- token-facing or foundation-facing page
- acts as part of the DS foundations surface

Current completeness:

- present
- not the main page used for the recent governance passes
- should continue to be treated as a foundations-facing page rather than a component API page

### `321:9714` — `组件Phase 0：基础层清理绑定优化`

Role:

- historical and operational governance page
- records the foundations cleanup and binding recovery work

Current completeness:

- high historical value
- not the right long-term canonical editing surface for day-to-day component authoring
- should be preserved as a cleanup and migration reference page

Key completed outcomes associated with this area:

- variable scope cleanup
- WEB code syntax cleanup
- semantic token backfills
- residual legacy binding cleanup across major families

### `3285:437` — `组件Phase 1: Component Schema Cleanup`

Role:

- historical and operational governance page for component cleanup
- main review board used for component API cleanup and page-local token/effect cleanup

Current completeness:

- high
- currently the most complete governance board in the file
- no longer just a temporary scratch board; it now serves as the most comprehensive cleanup reference page

Current quality state:

- component property naming significantly cleaned up
- effect styles fully styled on this page
- exact-match spacing/radius token coverage largely complete
- showcase labels normalized to `组件定义` and `组合示例`

Known intentional exceptions:

- board/showcase layout values
- fractional geometry values
- a few mixed padding cases requiring semantic judgment

Recommendation:

- preserve this page as a governance and review board
- do not treat it as the final canonical DS editing page forever

## 3. Emerging Canonical Component Pages

These pages now hold migration skeletons and are the natural candidates for becoming the canonical component pages.

### `3210:8207` — `原子组件/Navigation`

Current contents:

- `Nav`
- `Token list`
- `Menu`
- `beta`
- `Web nav`
- `Mobile nav`
- one example instance

Completeness:

- medium
- enough structure to start becoming a canonical navigation page
- still needs page-level normalization and example curation

### `3210:8201` — `原子组件/Button`

Current contents:

- `Button`
- `Button with blur`
- `Button-Web`
- `Token function bar`
- example instances

Completeness:

- highest among the target pages
- likely the closest page to becoming a canonical edit surface

### `3210:8199` — `原子组件/Modal`

Current contents:

- `Modal`
- example placeholder

Completeness:

- medium-low
- strong component definition exists
- example zone and page documentation still need curation

### `3210:8200` — `原子组件/Toast+Dialog`

Current contents:

- `Toast`
- `Toast-Web` example

Completeness:

- medium
- enough to continue hardening
- still needs page-level structure and scope clarification

### `3210:8205` — `原子组件/Toggle`

Current contents:

- `Toggle`
- example placeholder

Completeness:

- low to medium
- structural start exists
- needs stronger definition/example separation

### `3210:8203` — `原子组件/Backdrop`

Current contents:

- `Modal backdrop`
- `Bkg`
- example placeholder

Completeness:

- medium
- workable grouping, but still transitional

### `3210:8206` — `业务组件/Error`

Current contents:

- `Error` example

Completeness:

- medium-low
- acceptable as a business example page
- still needs clearer documentation of what belongs here vs in atomic pages

## 4. Current DS Semantics In Figma

The current Figma DS semantics are best understood across three layers of meaning:

### A. Foundation semantics

This includes:

- variable collections and modes
- text styles
- effect styles
- gradient and component-specific paint styles

Key state:

- local variables were normalized at the scope and code syntax level
- semantic gaps were backfilled where the existing DS surface required them
- text styles are already relatively canonical

### B. Governance semantics

This includes:

- the meaning of the Phase 0 and Phase 1 pages
- what counts as historical cleanup vs canonical DS definition

Current state:

- Phase 0 and Phase 1 pages are no longer just temporary scratch work
- they now hold important cleanup history and should be preserved
- but they should not remain the only operational edit surfaces forever

### C. Canonical component semantics

This includes:

- dedicated target pages for each atomic family
- separation of component definition and example usage
- stable public component APIs

Current state:

- this layer is emerging but not complete
- the new target pages are the right place to continue

## 5. Page Completeness Assessment

### Strongest pages right now

- `组件Phase 1: Component Schema Cleanup`
- `原子组件/Button`

### Most structurally important historical pages

- `组件Phase 0：基础层清理绑定优化`
- `组件Phase 1: Component Schema Cleanup`

### Most promising next canonical pages

- `原子组件/Button`
- `原子组件/Navigation`
- `原子组件/Modal`

### Pages that still need stronger curation

- `原子组件/Toggle`
- `原子组件/Backdrop`
- `业务组件/Error`

## 6. Recommended Next Step For The Pages

The next page-level work should not be broad file-wide cleanup. It should be a page-by-page hardening pass on the new target pages.

Recommended order:

1. `原子组件/Button`
   - likely first canonical component page
2. `原子组件/Navigation`
   - highest grouping complexity
3. `原子组件/Modal`
   - strongest API-driven family after Button
4. `原子组件/Toast+Dialog`
5. `原子组件/Backdrop`
6. `原子组件/Toggle`
7. `业务组件/Error`

## 7. Concrete Next Actions

### Action A: normalize each target page

For each target page:

- refine title and source labels
- ensure `组件定义` and `组合示例` structure is consistent
- reduce transitional placeholders where possible

### Action B: decide canonical edit surfaces

Explicitly decide:

- which pages are now canonical editing surfaces
- which pages remain historical governance references only

Recommended current canonical candidates:

- `原子组件/Button`
- `原子组件/Navigation`
- `原子组件/Modal`

### Action C: keep governance pages as references

Retain:

- `组件Phase 0：基础层清理绑定优化`
- `组件Phase 1: Component Schema Cleanup`

Use them as:

- cleanup history
- migration reference
- audit evidence

Not as:

- the only long-term DS editing surface

## 8. Short Recommendation

The DS file is now at a point where the next important move is not more generic cleanup. It is controlled canonization:

- keep Phase pages as historical governance surfaces
- continue hardening the target component pages
- promote a small number of those pages into true canonical edit surfaces

---

## 中文翻译

### 1. 当前 DS 页面结构

当前文件里的页面大致可以分成三类：

1. foundations 和 token 页面
2. 历史治理 / 清理页面
3. 正在形成中的 canonical component 页面

### 2. 主要页面及其角色

#### `1297:17025` — `Design token`

角色：

- foundations / token 侧页面
- 属于设计系统基础层的一部分

完整度：

- 页面存在
- 不是最近治理动作的主页面
- 后续应继续作为 foundations 页面使用，而不是组件 API 页面

#### `321:9714` — `组件Phase 0：基础层清理绑定优化`

角色：

- 历史治理页
- 记录 foundations 清理和绑定恢复

完整度：

- 历史价值高
- 不适合作为长期的日常组件编辑面
- 应保留为 cleanup / migration 参考页

这一页关联的主要成果：

- variable scope 清理
- WEB code syntax 清理
- semantic token 回填
- 多个核心 family 的 legacy binding 清理

#### `3285:437` — `组件Phase 1: Component Schema Cleanup`

角色：

- 历史治理页
- 最近 component API 清理和页面级 token/effect 清理的主 review 板

完整度：

- 很高
- 目前是文件里最完整的治理页
- 不再只是临时 scratch board，而是最完整的 cleanup reference

当前质量状态：

- component property naming 明显改善
- effect style 在此页已全覆盖
- spacing / radius 的 exact-match token 覆盖基本完成
- 展示标签已统一成 `组件定义` 和 `组合示例`

已知且刻意保留的例外：

- board/showcase 布局值
- fractional geometry 值
- 少量需要语义判断的 mixed padding 情况

建议：

- 保留它作为治理和 review 板
- 但不要永远把它当成最终 canonical DS 编辑页

### 3. 正在形成中的 canonical component 页面

这些页面已经有 migration skeleton，是最自然的下一步 canonical component page 候选。

#### `原子组件/Navigation`

当前内容：

- `Nav`
- `Token list`
- `Menu`
- `beta`
- `Web nav`
- `Mobile nav`
- 一个 example instance

完整度：

- 中等
- 已经足够作为 canonical navigation page 的起点
- 还需要页内规范化和 example 筛选

#### `原子组件/Button`

当前内容：

- `Button`
- `Button with blur`
- `Button-Web`
- `Token function bar`
- example instances

完整度：

- 是目标页里最高的
- 很可能是最接近 canonical edit surface 的页面

#### `原子组件/Modal`

当前内容：

- `Modal`
- example placeholder

完整度：

- 中低
- 组件定义本身已经较强
- example 区和页面说明还需要整理

#### `原子组件/Toast+Dialog`

当前内容：

- `Toast`
- `Toast-Web` example

完整度：

- 中等
- 可以继续 harden
- 还需要更明确的 page-level 结构和 scope

#### `原子组件/Toggle`

当前内容：

- `Toggle`
- example placeholder

完整度：

- 低到中
- 已经有结构起点
- 还需要更明确地区分 definition 和 example

#### `原子组件/Backdrop`

当前内容：

- `Modal backdrop`
- `Bkg`
- example placeholder

完整度：

- 中等
- 分组合理，但仍是过渡状态

#### `业务组件/Error`

当前内容：

- `Error` example

完整度：

- 中低
- 可接受为业务示例页
- 但仍需更清楚说明哪些内容应留在这里，哪些应归到 atomic pages

### 4. 当前 Figma 里的 DS 语义

当前 Figma 里的 DS 语义最好分三层看：

#### A. Foundation semantics

包括：

- variable collections 和 modes
- text styles
- effect styles
- gradient 和 component-specific paint styles

当前状态：

- 本地变量在 scope 和 code syntax 层面已被规范化
- 现有 DS surface 需要的 semantic gap 已补齐
- text styles 已相对 canonical

#### B. Governance semantics

包括：

- Phase 0 和 Phase 1 页面分别代表什么
- 什么算历史治理页，什么算 canonical DS 定义页

当前状态：

- Phase 0 / Phase 1 已不是简单的临时草稿
- 它们承载了重要治理历史，应保留
- 但不应长期成为唯一的 operational edit surface

#### C. Canonical component semantics

包括：

- 每个 atomic family 的专用目标页
- component definition 和 example usage 的分离
- 稳定的 public component API

当前状态：

- 这一层正在形成，但尚未完全成熟
- 新目标页是正确的继续推进位置

### 5. 页面完整度判断

当前最强的页面：

- `组件Phase 1: Component Schema Cleanup`
- `原子组件/Button`

当前最重要的历史治理页：

- `组件Phase 0：基础层清理绑定优化`
- `组件Phase 1: Component Schema Cleanup`

最值得继续扶正的 canonical component 页：

- `原子组件/Button`
- `原子组件/Navigation`
- `原子组件/Modal`

仍需更多整理的页面：

- `原子组件/Toggle`
- `原子组件/Backdrop`
- `业务组件/Error`

### 6. 下一步页面级建议

下一步不应该继续做泛化的全文件 cleanup，而是逐页硬化这些新目标页。

建议顺序：

1. `原子组件/Button`
2. `原子组件/Navigation`
3. `原子组件/Modal`
4. `原子组件/Toast+Dialog`
5. `原子组件/Backdrop`
6. `原子组件/Toggle`
7. `业务组件/Error`

### 7. 具体动作

#### A. 规范每个目标页

对每个目标页：

- 优化标题和 source 标记
- 统一 `组件定义` / `组合示例` 的结构
- 尽量减少 placeholder

#### B. 明确 canonical edit surfaces

明确判断：

- 哪些页是 canonical editing surfaces
- 哪些页只保留为历史治理参考

当前建议的 canonical 候选：

- `原子组件/Button`
- `原子组件/Navigation`
- `原子组件/Modal`

#### C. 保留治理页作为参考

保留：

- `组件Phase 0：基础层清理绑定优化`
- `组件Phase 1: Component Schema Cleanup`

用途：

- cleanup history
- migration reference
- audit evidence

而不是：

- 唯一的长期 DS 编辑面

### 8. 简短结论

当前 DS 文件已经进入一个新的阶段：接下来最重要的不是继续做泛 cleanup，而是受控地“扶正” canonical 页面。

- 保留 Phase 页作为治理历史
- 继续强化目标组件页
- 从中挑出少量页面，正式升级成 canonical edit surfaces
