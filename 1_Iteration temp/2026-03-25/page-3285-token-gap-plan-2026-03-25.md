# Page 3285 Token Coverage Plan

Date: 2026-03-25

Target page:
`3285:437` / `组件Phase 1: Component Schema Cleanup`

## Completed In This Pass

- kept `component/button/primary/fill` and `component/button/primary/stroke`
- converged effect-style naming under a single `effect/...` namespace
- applied effect styles so the page now has:
  - `59` effect-bearing nodes
  - `59` styled nodes
  - `0` bare effects
- applied exact-match number token bindings for low-risk cases:
  - spacing: `4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 42 / 72`
  - radius: `4 / 10 / 16`
  - full radius mapping for repeated pill-like uniform radii above `16`

## Current Effect Style Namespace

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

## Remaining Untokenized Structure Values

These are the remaining high-signal groups after the exact-match binding pass.

### Likely missing token values

- `itemSpacing:10` × 48
- `itemSpacing:14` × 8
- `itemSpacing:62` × 8
- `itemSpacing:2` × 4
- `itemSpacing:48` × 2
- `itemSpacing:15` × 2
- `itemSpacing:23` × 1
- `radius:8` × 1

### Likely board/layout exceptions or values that need deliberate normalization

- `itemSpacing:248` × 3
- `itemSpacing:1151` × 2
- `itemSpacing:56` × 2
- `itemSpacing:7.778` × 1

### Fractional geometry values that should not be tokenized blindly

- `radius:0.762...` × 3
- `radius:0.508...` × 1

### Partial padding bindings still missing because only some sides match tokens

- `padding:2/8/2/8` missing `top,bottom` × 2
- `padding:10/16/10/16` missing `top,bottom` × 2
- `padding:9/24/9/24` missing `top,bottom` × 1
- `padding:16/56/16/56` missing `right,left` × 1

## Recommended Next Phase

### Phase A: add missing reusable primitives

Recommended additions:

- spacing:
  - `spacing/2`
  - `spacing/10`
  - `spacing/14`
  - `spacing/15`
  - `spacing/48`
  - `spacing/62`
- radius:
  - `radius/xs = 8`

### Phase B: bind the new primitives on this page

After the new tokens exist, bind:

- the repeated `10 / 14 / 15 / 48 / 62 / 2` gaps
- the one remaining `radius:8`
- the partial padding cases where the missing sides correspond to new spacing tokens

### Phase C: handle page-scaffold exceptions explicitly

These values should be treated as page-composition or showcase-layout exceptions unless you explicitly want board layout tokenized:

- `248`
- `1151`
- `56`
- `7.778`

### Phase D: normalize rather than tokenize fractional geometry

Do not create tokens for:

- `0.508`
- `0.762`

These should be reviewed as geometry artifacts and either:

- snapped to `0`
- snapped to `4`
- or preserved as implementation-specific shapes
