# Figma DS Cleanup Progress

Date: 2026-03-25

Target Figma file:
`DBQdb8ymhIfTPS9GmcTqaR`

## Completed

- Normalized local variable `scope` and `WEB code syntax` for the current local variable model.
- Created missing semantic token:
  - `Semantic/text/inverse`
- Backfilled the same token into:
  - `Iteration temp/source_token_v5.json`
- Normalized `Button` component family:
  - variant naming moved to `Variant=` / `State=`
  - typo fixed: `horitontal` -> `horizontal`
  - primary button paints were consolidated into local paint styles
  - labels were rebound to local text styles and local semantic text variables
- Normalized `Button-Web` basic naming and text style usage.
- Rebound obvious legacy remote color bindings to current local variables across:
  - `Modal`
  - `Nav`
  - `Web nav`
  - `Toast`
  - `Menu`
  - `Mobile nav`
  - `Breadcrumb`
- Finished the residual cleanup pass and rebound the last legacy or non-canonical bindings across:
  - `Button`
  - `Modal`
  - `Nav`
  - `Web nav`
  - `Mobile nav`
  - `Menu`
  - `Token list`
  - `Toggle`
- Applied local typography styles across the core component sets so components are no longer primarily dependent on old remote text styles.

## Residual Nonlocal Bindings

Current status after the final audit:

- total residual bindings across the audited component sets: `0`
- audited families:
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

## Generated / Added During Cleanup

- `Semantic/text/inverse`
  - created in Figma
  - added to `Iteration temp/source_token_v5.json`
  - reason: primary button and similar dark-surface controls needed a canonical inverse text token and the source file did not have one
- `Semantic/fill/action`
  - created in Figma
  - added to `Iteration temp/source_token_v5.json`
  - reason: legacy bright-blue action fills in modal token circles and similar accents had no canonical semantic fill token
- `Semantic/fill/action_subtle`
  - created in Figma
  - added to `Iteration temp/source_token_v5.json`
  - reason: pale-blue action/account chips in web navigation had no canonical semantic subtle fill token
- `Semantic/stroke/logo`
  - created in Figma
  - added to `Iteration temp/source_token_v5.json`
  - reason: token-logo and brand-outline strokes were using legacy remote variables and needed a canonical semantic stroke
- `Semantic/stroke/icon_inverse`
  - created in Figma
  - added to `Iteration temp/source_token_v5.json`
  - reason: primary button icons were using a legacy inverse stroke token and needed a canonical semantic replacement

## Interpretation

The Figma file is now materially cleaner than the starting point:

- foundations are more schema-aligned
- core typography is local
- stale remote and non-canonical color-variable usage in the audited component sets was removed
- `Button` is now much closer to a canonical component family

The audited component families are now converged on the current local semantic layer for fills, text, strokes, borders, and gradient styles.

## Recommended Next Pass

1. standardize remaining component names, variant axes, and auto-layout quality outside the already-touched families
2. audit existing local text styles and effect styles against the same canonical semantic model
3. decide whether `Pattern` and `Component` variable collections should be retained, reduced, or migrated further toward a stricter `Primitive` + `Semantic` split
4. run a broader file-level audit beyond the current core component-set page if other pages or detached examples need the same cleanup
