# WebApp DS v2 Design Guide

## Structure

This document describes the current WebApp DS v2 visual system as reflected by:

- the design token foundation page at `Design token sheet` (`node-id=1297:17025`)
- the canonical component pages under `原子组件/*`
- the canonical Figma button page at `原子组件/Button` (`node-id=3210:8201`)
- the active source token file at `source/tokens.json`
- the runtime and Figma adapter outputs in `adapters/runtime` and `adapters/figma`
- the current demo implementations in `Iteration temp`

This guide is intentionally system-facing rather than inspirational. It is designed to help:

- AI read the current design language correctly
- designers keep Figma aligned with the token system
- engineers translate Figma into production code with fewer guesses

## Current Condition

The existing `design md/DESIGN.md` describes an Airbnb-inspired marketplace system and no longer matches the current WebApp DS v2 implementation direction.

The current system shown in Figma is a finance-oriented, action-heavy interface with these observable traits:

- a blue-led primary action language
- navy-first text and secondary emphasis in light mode
- soft light gradients and glass/blur surfaces
- mobile-first button families with web variants
- compact, rounded controls optimized for transactional flows

The currently linked canonical pages expose these component areas:

- `原子组件/Navigation`
- `原子组件/Button`
- `原子组件/Modal`
- `原子组件/Toast+Dialog`
- `原子组件/Toggle`
- `原子组件/Backdrop`

The token-sheet page additionally exposes the current foundation system:

- primitive colors
- semantic colors
- typography scale
- spacing and size scale
- radius scale
- shadow scale

The button page currently exposes four button-related families:

- `Button`
- `Button with blur`
- `Button-Web`
- `Token function bar`

Observed variant coverage on that page includes:

- primary, secondary, short, mini, micro, processing
- double-horizontal and double-vertical action arrangements
- blur-backed grouped actions
- web-specific horizontal and vertical action bars
- token function bar variants for default and redirection

There is also a system gap that should be treated as active drift:

- the visual primary button language in Figma is a bright blue gradient
- the current component token alias in `source/tokens.json` still maps `component.button.primary.default.background` to `semantic.fill.secondary`
- the runtime adapter still reports button radius as `[MISSING]`
- some component families are canonical in Figma but not yet formalized in `component.md`

## Recommended Next Move

- treat this document as the current visual reference for WebApp DS v2, not the older Airbnb document
- keep Figma as the authoring surface for component organization and visual shape
- align token aliases so primary button recipes match the blue gradient system already visible in Figma and demos
- add explicit semantic roles for on-primary text, gradient button surfaces, and blur-backed grouped action patterns
- use `component.md` to lock component contract names after a family is visually stable in Figma

---

## 1. Visual Theme

WebApp DS v2 is a polished transactional interface system rather than a content-browsing system. The visual tone is clean, precise, and optimistic. White and near-white surfaces dominate the light theme, with brand blue used as the main activation signal and navy used for dense text and secondary solid controls.

The system feels lightweight rather than heavy. It avoids thick borders, dark blocks, and aggressive shadows. The dominant effect language is:

- soft vertical gradients
- high-radius pills and rounded cards
- light glass blur for elevated grouped actions
- bright but controlled action emphasis

The overall impression should be:

- trustworthy
- efficient
- slightly futuristic
- suitable for wallet, asset, and token flows

## 2. Color System

### Primary Roles

- Primary action blue: `#007FFF`
- Deep action blue for dark surfaces: `#066BD2`
- Core navy text and fill: `#111D4A`
- General white surface: `#FFFFFF`
- Soft page gray: `#F0F1F3`
- Modal gray: `#F9FAFB`

### Supporting Status Roles

- Success: `#4BCE71`
- Error: `#F3636F`
- Warning: `#FC8C4D`

### Light Theme Behavior

The light theme uses navy as the highest-contrast text and secondary fill color, not black. Blue is the main action cue. Page surfaces are rarely flat white only; they often sit on a soft light gradient or a pale blue-tinted field.

Preferred light-theme roles from the token system:

- `semantic.background.general`
- `semantic.background.card`
- `semantic.background.modal`
- `semantic.text.core`
- `semantic.text.primary`
- `semantic.text.secondary`
- `semantic.text.action`
- `semantic.border.default`

### Dark Theme Behavior

The dark theme uses near-black and deep gray surfaces rather than saturated brand-heavy panels. Blue remains the action accent, but is adapted for dark backgrounds. Dark mode should still feel crisp and technical, not neon.

Preferred dark-theme references:

- `gray.900`, `gray.800`, `gray.950`
- `blue.600`
- `gray.350`, `gray.450`

### Important Drift Note

The token system currently models several solid fills well, but the visible Figma button family and demo files already rely on a brighter gradient-led primary action treatment. That gradient needs to be formalized as a first-class design-system surface rather than left as a local visual effect.

## 3. Gradient And Blur Language

Gradient and blur are not decorative extras in this system. They are part of the interaction hierarchy.

### Canonical Gradient Roles

- `semantic.gradient.general`
  Light page atmosphere, soft blue-to-gray vertical field
- `semantic.gradient.main`
  Hero or branded section depth
- `semantic.gradient.xaut_card`
  Frosted action card or asset highlight treatment
- `semantic.gradient.bar_backdrop`
  Feathered navigation and bar backdrop

### Practical Usage

- Use soft vertical gradients for page shells and large header zones
- Use stronger blue radial or vertical gradients for high-priority CTAs
- Use blur-backed grouped action containers when the action block floats above active content
- Keep blur surfaces bright, translucent, and restrained

Do not:

- use random multi-color gradients
- use blur as a substitute for hierarchy
- apply strong shadows and strong blur at the same time on every surface

## 4. Typography

The runtime typography output shows a Noto Sans-based system with a narrow, practical hierarchy. This is appropriate for transactional UI and current demos.

### Current Text Roles

- `heroTitle`
  32px, 700, 140%
- `heroAmount`
  24px, 700, 140%
- `sectionLead`
  20px, 500, 140%
- `navTitle`
  16px, 700, 140%
- `bodyPrimary`
  16px, 500, 140%
- `actionLabel`
  16px, 400, 140%
- `bodySecondary`
  14px, 400, 140%

### Typography Character

This system is not editorial. It is operational:

- numbers and balances should feel stable and legible
- section titles should feel firm but not oversized
- button labels should stay clean and short
- secondary text should recede without becoming faint noise

### Recommendation

The typography scale is workable, but action labels should be reviewed. The current `actionLabel` weight of `400` is serviceable, but several button surfaces in Figma visually read as needing stronger emphasis, especially against bright gradient fills. If Figma consistently uses a heavier label treatment, the semantic typography alias should be updated to match.

## 5. Shape, Radius, And Sizing

The current system uses rounded geometry as a core signal of friendliness and touch readiness.

Canonical size and radius references from tokens:

- `primitive.radius.sm = 4`
- `primitive.radius.md = 10`
- `primitive.radius.lg = 16`
- `primitive.radius.full = 9999`

Common control heights in the current system:

- `30px` micro
- `36px` mini
- `48px` medium controls
- `52px` primary CTA
- `54px` web primary variants in Figma examples

Preferred usage:

- pills and CTAs: full or near-full rounding
- modals and cards: `16px`
- compact utility controls: `4px` to `10px`

## 6. Button Family

The linked Figma page makes the button family the clearest canonical surface in the current library.

### Core Button Types

- Primary
- Secondary
- Primary short
- Secondary short
- Primary mini
- Primary micro
- Processing
- Double horizontal
- Double vertical

### Blur-Backed Action Group Types

- without text
- with text
- with tips
- double vertical

### Web Button Types

- primary
- secondary
- horizontal with blur
- vertical with blur
- vertical without blur

### Button Behavior Principles

- primary actions should dominate through blue emphasis, not extra size alone
- secondary actions should remain clearly available without competing with the primary CTA
- grouped actions should preserve hierarchy between confirm and back/cancel paths
- processing states should reduce ambiguity, not simply dim the control
- mini and micro variants should be used only when task density justifies them

### Current Styling Read

In Figma and demos, primary actions read as:

- bright blue gradient or strong blue emphasis
- white label text
- high-radius pill shape
- compact horizontal padding

Secondary actions read as:

- white or light surface
- navy or muted text
- subtle border
- same geometry family as primary

This means the current runtime aliasing for button color should be revisited so the system definition matches the visible component family.

## 7. Navigation And Menu Family

The `原子组件/Navigation` page shows a mature navigation family rather than isolated one-off examples.

### Observed Subfamilies

- `Navigation / web shell`
- `Token list / navigation tokens`
- `Account menu`
- `Beta badge`
- `Web navigation`
- `Mobile navigation`

### Observed Variants

- web shell: `State=Default`, `State=Token main scroll`
- token list control: `State=Default`, `State=Expanded`
- account menu: `Auth state=Signed out`, `Auth state=Signed in`
- web navigation: `Auth state=Signed out`, `Auth state=Signed in`
- mobile navigation: `Level=Primary`, `Level=Secondary`

### System Read

This family reinforces several system rules:

- navigation is mode-aware and auth-aware
- mobile and web shells share one visual language, but not one geometry
- token list controls are treated as navigational affordances, not generic pills
- small utility badges such as `Beta` belong in the same family of rounded, token-aware affordances

The mobile navigation shell and secondary navigation bar shown in demos should therefore be treated as canonical component patterns, not page-only chrome.

## 8. Modal, Dialog, And Backdrop Family

The current canonical surfaces separate content container, feedback overlay, and background treatment instead of collapsing them into one undifferentiated modal asset.

### Modal Page Coverage

The `原子组件/Modal` page includes:

- `Type=Default, Platform=Mobile`
- `Type=Default with subtitle, Platform=Mobile`
- `Type=Level 2, Platform=Mobile`
- `Type=Dialog, Platform=Mobile`
- `Type=Default, Platform=Web`
- `Type=Dialog, Platform=Web`
- `Type=Tour, Platform=Mobile`
- `Type=Tour, Platform=Web`

### Backdrop Page Coverage

The `原子组件/Backdrop` page includes:

- modal backdrop: `Type=Default`
- background surfaces: `Type=General bkg`, `Type=Token main`

### System Read

This family suggests:

- modal is a platform-aware container family
- dialog is a subtype rather than a completely separate visual language
- tour surfaces are part of the same elevation and radius system
- backdrop and page background are separate DS assets and should stay explicit in code

This is a good sign for AI-to-code work because it reduces the need to infer overlay behavior from screenshots alone.

## 9. Toast And Toggle Family

Two smaller families are also already canonical and should be included in the system view.

### Toast

The `原子组件/Toast+Dialog` page currently exposes:

- `Type=Max width`
- `Type=Adaptive`
- example instance: `Toast-Web`

The current Figma surface reads more like a toast-only canonical page than a combined dialog system page. Naming should likely be tightened later if dialog variants remain absent.

### Toggle

The `原子组件/Toggle` page currently exposes:

- `Status=On`
- `Status=Off`

This is a small family, but it is already good candidate material for an early component contract because the API surface is narrow and stable.

## 10. Navigation And Bars

Although the linked node is button-scoped, the repo demos show a repeated bar and navigation language that should be treated as part of the current design grammar.

Observed patterns:

- 90px primary nav shell on mobile
- white-to-transparent top gradient bar backdrop
- 56px secondary nav with blur and subtle border
- center-weighted title treatment
- icon buttons on circular or invisible hit areas

This navigation language supports wallet and send-token style flows where chrome should feel present but not heavy.

## 11. Spacing And Composition

The active spacing scale in tokens is disciplined and should remain the default system:

- `4`
- `8`
- `12`
- `16`
- `20`
- `24`
- `32`
- `40`
- `42`
- `72`

### Composition Principles

- use `16px` as the standard inner padding unit
- use `12px` for compact row gaps and field internals
- use `32px` for clear action-group or section separation
- reserve `72px` for modal content offsets and deliberate top gaps

The current system is mobile-first and transactional. Layouts should feel compact, but not cramped. The space model should support fast scanning of:

- balances
- token rows
- confirmation steps
- grouped action bars

## 12. Responsive Behavior

The current Figma evidence is strongest on mobile and action-bar variants, with some explicit web button variants.

The intended responsive pattern is:

- mobile-first sizing and grouped controls
- wider web buttons with the same visual language
- grouped vertical and horizontal button arrangements that scale by context

When implementing beyond the linked node:

- preserve the same CTA hierarchy between mobile and web
- do not flatten blur-backed action groups into generic stacked buttons
- keep the same radius and visual weight family between platforms

## 13. Component Inventory Snapshot

Based on the currently scanned canonical pages, the existing DS families visible through MCP are:

- foundation sheet
- navigation
- token-list navigation control
- account menu
- beta badge
- web navigation
- mobile navigation
- button
- blur-backed button group
- web button
- token function bar
- modal
- dialog
- tour modal
- backdrop
- page background shell
- toast
- toggle

This is not yet a full-file inventory. It is the current confirmed canonical set based on the linked nodes.

## 14. Agent Guidance

When AI generates UI from this system, it should assume:

- this is a wallet/productivity transactional system, not editorial content UI
- blue is the main activation color
- navy is the main text and secondary emphasis color
- gradients and blur are systematic, not incidental
- mobile action density is a first-class design constraint
- button grouping patterns are reusable assets, not one-off mockups

Use:

- semantic tokens for color and text roles
- primitive scales for spacing, radius, and size
- component contracts for variant naming and behavior

Avoid:

- inventing new accent colors
- replacing rounded pills with square enterprise controls
- translating blur-backed groups into plain white cards without reason
- assuming the older Airbnb document is still the active reference

## 15. System Gaps To Resolve

This guide fits the current Figma surface, but several system definitions still need to catch up:

- formalize a semantic role for primary gradient CTA surfaces
- add explicit semantic roles for on-primary and on-danger text
- align button component aliases with current Figma variants
- fix missing radius propagation in runtime adapter outputs
- document `Navigation`, `Modal`, `Backdrop`, `Toast`, and `Toggle` as explicit component families in `component.md`
- tighten naming on pages where the page title and actual canonical contents no longer fully match

## 16. Canonical Scope Note

This document is grounded in the currently linked Figma node and the active repo artifacts. It should be treated as the current guide for the button family and adjacent action surfaces.

At this point, the confirmed canonical set already covers:

- foundation tokens
- button and grouped actions
- navigation and menu surfaces
- modal, dialog, and backdrop
- toast
- toggle

The next likely pages to add are:

- Input
- Form field patterns
- token list rows
- cards and detail panels
- table or data-heavy web surfaces
