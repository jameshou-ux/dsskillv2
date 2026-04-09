# Design System — alpha.token.im

## 1. Visual Theme & Atmosphere

alpha.token.im is a verifiable generative UI wallet where users keep full asset sovereignty while experiencing near-zero blockchain complexity. The design language reflects this dual nature: it is calm and trustworthy enough for a financial interface, yet light and modern enough to feel like a consumer app. Every design decision serves the product principles — tokens over chains, clarity over chrome, and human control over automation.

The visual identity is built on a clean, luminous aesthetic. Light surfaces (`#fafaf9`, `#ffffff`) dominate the canvas, providing an open and breathable backdrop for dense financial data. A single brand blue (`#007fff`) serves as the primary interactive accent, applied consistently to CTAs, focus rings, active states, and brand gradient moments. A secondary cyan (`#0cc5ff`) adds depth to the brand palette without competing for attention. Together they form a controlled two-tone blue identity that signals trust and technology without the clinical coldness of a banking app.

Typography is anchored in **Noto Sans Variable** — a clean, humanist sans-serif with full optical-sizing support. Its variable-weight axis allows fluid transitions from bold 700 display headlines down to regular 400 body text, all from the same typeface family. Chinese content falls back to **Noto Sans SC** with pre-loaded weights at 400, 600, and 700 for consistent rendering.

Dark mode is not an afterthought — it is a first-class citizen. The dark palette (`#0a0b0d` background, `#282b31` card surfaces, `rgba(255, 255, 255, 0.6)` secondary text) is designed for immersive, low-light trading sessions where the brand blue pops against deep neutrals.

**Key Characteristics:**
- Noto Sans Variable with optical sizing — one typeface adapts fluidly across all sizes
- Luminous light theme: warm off-white `#fafaf9` page surface with pure `#ffffff` card surfaces
- Single brand accent: Primary Blue `#007fff` reserved for all interactive and brand elements
- Secondary accent: Cyan `#0cc5ff` for supporting brand moments and visual interest
- Token-centric data display — financial information presented in clean, scannable layouts
- Generous rounded corners (12–20px on cards, full pill on CTAs) creating a soft, approachable feel
- Soft, layered shadows using the brand navy (`rgba(17, 29, 74, *)`) for depth that feels organic
- 8px spacing grid with strict adherence across all components
- Dark mode as equal citizen — deep near-black `#0a0b0d` with elevated card surfaces at `#282b31`

## 2. Color Palette & Roles

### Brand

- **Primary Blue** (`#007fff`): `--primary`, `--brand`. The singular interactive accent — CTAs, focus rings, active navigation, progress bars, links. This is the identity color.
- **Cyan** (`#0cc5ff`): `--accent`, `--brand-secondary`. Secondary brand color for gradients, highlights, and accent moments. Never competes with Primary Blue for CTA attention.
- **Brand Hover** (`#66b2ff`): `--brand-hover`. Lighter blue for hover states on brand elements.

### Surfaces — Light

- **Page Background** (`#fafaf9`): `--surface-page`. The base canvas — a warm off-white that prevents the sterile feel of pure white.
- **Card White** (`#ffffff`): `--background`, `--card`. Clean white for elevated card surfaces and content containers.
- **Cool Surface** (`#f2f6fb`): `--surface-cool`. Blue-tinted light surface for subtle section differentiation.
- **Soft Surface** (`rgba(247, 247, 247, 0.88)`): `--surface-light`. Semi-transparent light surface for overlay contexts.
- **Secondary** (`#f0f1f3`): `--secondary`, `--muted`. Neutral gray for secondary buttons, muted backgrounds, and inactive states.
- **Surface Blue** (`#f8fafe`): `--surface-blue`. Very light blue wash for feature highlights and info backgrounds.
- **Surface Blue Light** (`#f2f6ff`): `--surface-blue-light`. Badge backgrounds, subtle blue tint areas.
- **Surface Blue Dim** (`#eff6ff`): `--surface-blue-dim`. Softer blue surface for icon containers.
- **Surface Blue Info** (`#eef5ff`): `--surface-blue-info`. Informational blue surface backgrounds.

### Surfaces — Dark

- **Dark Background** (`#0a0b0d`): `--dark-surface`, dark `--background`. The deepest canvas in dark mode.
- **Dark Card** (`#282b31`): Dark `--card`, `--secondary`, `--muted`. Elevated surface in dark mode.
- **Dark Surface Blue** (`#1a1e2e`): Dark mode equivalent of blue-tinted surfaces.

### Text — Light

- **Foreground** (`#111d4a`): `--foreground`. Primary heading and body text on light backgrounds — a deep navy-black that is warmer than pure black.
- **Secondary Foreground** (`#111d4a`): `--secondary-foreground`. Matches foreground on secondary surfaces.
- **Muted Foreground** (`#717182`): `--muted-foreground`. Secondary text, descriptions, labels — a balanced mid-gray.
- **Tertiary** (`#99a1af`): `--text-tertiary`. Placeholder text, least-prominent labels.
- **Secondary Gray** (`#475467`): `--text-secondary-gray`. Slightly darker than muted, for important secondary info.

### Text — Dark

- **Foreground** (`#ffffff`): Dark `--foreground`. Primary text on dark backgrounds.
- **Muted Foreground** (`rgba(255, 255, 255, 0.6)`): Dark `--muted-foreground`. Secondary text in dark mode.
- **Tertiary** (`rgba(255, 255, 255, 0.4)`): Dark `--text-tertiary`. Low-prominence labels in dark mode.
- **Secondary Gray** (`rgba(255, 255, 255, 0.6)`): Dark `--text-secondary-gray`.

### Semantic — Interactive

- **Primary** (`#007fff`): `--primary`. Button fills, active states, links.
- **Primary Foreground** (`#ffffff`): `--primary-foreground`. Text on primary-colored surfaces.
- **Accent Foreground** (`#ffffff`): `--accent-foreground`. Text on accent-colored surfaces.
- **Ring** (`#007fff`): `--ring`. Focus ring color — matches primary for consistent interactive language.

### Semantic — Feedback

- **Success** (`#10b981`): `--success`. Completed states, positive confirmations.
- **Success Text** (`#0f9f6e` light / `#34d399` dark): `--success-text`. Text-optimized success color.
- **Success Surface** (`#ecfdf5` light / `rgba(16, 185, 129, 0.12)` dark): `--success-surface`. Background tint for success states.
- **Success Border** (`#b6e3cf` light / `rgba(16, 185, 129, 0.24)` dark): `--success-border`. Subtle border for success cards.
- **Success Surface Tint** (`#f2fcf7` light / `rgba(16, 185, 129, 0.06)` dark): `--success-surface-tint`. Very light success wash for completed step cards.
- **Positive** (`#00a63e` light / `#34d399` dark): `--positive`. Profit, gains, positive P&L values.
- **Positive Surface** (`#f0fdf4` light / `rgba(16, 185, 129, 0.08)` dark): `--positive-surface`. Background for positive badges.
- **Destructive** (`#d4183d` light / `#fb2c36` dark): `--destructive`. Errors, dangerous actions, negative states.

### Borders

- **Border** (`rgba(17, 29, 74, 0.08)` light / `rgba(255, 255, 255, 0.1)` dark): `--border`. Default border color — barely visible, structurally defining.
- **Input Border** (`rgba(17, 29, 74, 0.08)` light / `rgba(255, 255, 255, 0.15)` dark): `--input`. Input field borders — slightly more visible in dark mode.
- **Info Border** (`#d8e8ff` light / `rgba(0, 127, 255, 0.2)` dark): `--info-border`. Active step card borders, informational highlights.

### Charts

| Token | Light | Dark |
|-------|-------|------|
| `--chart-1` | `#007fff` | `#007fff` |
| `--chart-2` | `#0cc5ff` | `#0cc5ff` |
| `--chart-3` | `#66b2ff` | `#66b2ff` |
| `--chart-4` | `#f2f6fb` | `#282b31` |
| `--chart-5` | `#111d4a` | `#f2f6fb` |

## 3. Typography Rules

### Font Family

- **Primary**: `"Noto Sans Variable", "Noto Sans", ui-sans-serif, system-ui, -apple-system, sans-serif` — `--font-sans`
- **Heading**: Same as primary — `--font-heading`. No separate display font; weight and size create hierarchy.
- **Chinese**: `"Noto Sans SC", "Noto Sans Variable", "Noto Sans", ui-sans-serif, system-ui, sans-serif` — `--font-chinese`

### Rendering

- `text-rendering: optimizeLegibility`
- `-webkit-font-smoothing: antialiased`
- `-moz-osx-font-smoothing: grayscale`

### Hierarchy

| Role | Size | Weight | Line Height | Tracking | Token / Notes |
|------|------|--------|-------------|----------|---------------|
| Display / Hero | 40px (2.5rem) | 700 | 1.0 (tight) | tight | Balance displays, hero numbers |
| Page Title | 24px (1.5rem) | 700 | 1.2 | tight | Page headings |
| Section Title | 20px (1.25rem) | 700 | 1.3 | tight | Section headings within pages |
| Card Title | 16px (1rem) | 600 | 1.4 (snug) | normal | `CardTitle`, panel headings |
| Body Large | 15px (0.9375rem) | 600–700 | 1.4 | normal | `--text-sm-plus` — bold labels, step card labels |
| Body | 14px (0.875rem) | 400–600 | 1.5 | normal | Standard reading text, descriptions |
| Body Small | 13px (0.8125rem) | 400–500 | 1.5 (relaxed) | normal | `--text-xs-plus` — chat bubbles, stat values |
| Caption | 12px (0.75rem) | 400–600 | 1.33 | normal | Labels, progress text, stat labels |
| Micro | 11px (0.6875rem) | 400–600 | 1.33 | normal | `--text-2xs` — stat cell labels, smallest text |
| Uppercase Label | 11px | 600 | 1.0 | 0.08em | Balance section label ("UNIFIED BALANCE") |

### Extended Font Sizes

| Token | Value | Use |
|-------|-------|-----|
| `--text-2xs` | 0.6875rem (11px) | Micro labels, stat cell labels |
| `--text-xs-plus` | 0.8125rem (13px) | Chat bubbles, descriptions, secondary info |
| `--text-sm-plus` | 0.9375rem (15px) | Step card labels, emphasized body text |

### Principles

- **Single family, variable weight**: Noto Sans Variable covers the full 100–900 weight axis. The design system uses 400 (regular), 600 (semibold), and 700 (bold). No other weights appear in components.
- **Size creates hierarchy, not font swapping**: All text uses the same typeface family. Hierarchy is established through size differences (11px to 40px), weight contrasts (400 vs 700), and color opacity shifts.
- **Tight headings, relaxed body**: Display and title text uses tight leading (1.0–1.3) for density and impact. Body text opens to 1.5 line-height for comfortable reading. Chat bubbles use `leading-relaxed`.
- **Semibold as workhorse**: Most emphasis uses weight 600 (semibold) rather than 700 (bold). Bold is reserved for primary headings and financial numbers.

## 4. Component Stylings

### Button

**Primary (Default CTA)**
- Background: `--primary` (`#007fff`)
- Text: `--primary-foreground` (`#ffffff`)
- Shadow: `--shadow-cta-sm` (`0 4px 14px rgba(0, 127, 255, 0.22)`)
- Shape: `rounded-full` (pill)
- Height: 40px (default), 48px (lg), 56px (hero)
- Font: 14px, weight 500
- Hover: brightness shift
- Focus: `--ring` outline
- Hero variant: larger shadow `--shadow-cta` (`0 8px 28px rgba(0, 127, 255, 0.28)`)

**Secondary**
- Background: `--secondary` (`#f0f1f3`)
- Text: `--secondary-foreground` (`#111d4a`)
- Shape: `rounded-full`
- Shadow: none
- Use: Secondary actions alongside Primary

**Outline**
- Background: transparent
- Border: 1px solid `--border`
- Shape: `rounded-full`
- Use: Tertiary actions, less emphasis

**Ghost**
- Background: transparent
- Text: `--muted-foreground`
- Hover: `foreground/6` background tint
- Shape: `rounded-full`
- Use: Toolbar actions, subtle interactions

**Foreground**
- Background: `--foreground` (`#111d4a` / `#ffffff`)
- Text: `--background` (inverse)
- Shape: `rounded-full`
- Use: High-contrast inverse CTA

**Destructive**
- Text: `--destructive` (`#d4183d`)
- Background: transparent
- Use: Dangerous actions (close, delete)

**Link**
- Text: `--primary` (`#007fff`)
- Underline on hover, offset 4px
- Use: Inline text links

**Size Scale**

| Size | Height | Padding | Font |
|------|--------|---------|------|
| `hero` | 56px (h-14) | px-8 | 16px, semibold |
| `lg` | 48px (h-12) | px-6 | 14px, semibold |
| `default` | 40px (h-10) | px-5 | 14px, medium |
| `sm` | 32px (h-8) | px-4 | 12px, medium |
| `xs` | auto | px-3, py-2 | 12px, medium |
| `icon` | 36px (size-9) | — | — |
| `icon-sm` | 32px (size-8) | — | — |

### IconButton

Circular icon-only buttons for toolbar and nav actions.

| Variant | Background | Icon Color |
|---------|------------|------------|
| `ghost` | transparent → `foreground/6` on hover | `--text-tertiary` |
| `muted` | `--secondary` | `--secondary-foreground` |
| `foreground` | `--foreground` | `--background` |

| Size | Dimensions | Icon Size |
|------|------------|-----------|
| `sm` | 36×36px | 16px |
| `md` | 40×40px | 20px |
| `lg` | 48×48px | 20px |

### ActionButton & ActionBar

Full-width action buttons arranged in a responsive grid.

- **Primary**: `--primary` background, `--primary-foreground` text, `--shadow-cta-sm` shadow
- **Secondary**: `--secondary` background, `--secondary-foreground` text
- Height: 48px (h-12), `rounded-full`, semibold 14px
- Icon: 16px with stroke-width 2.5
- Grid: 2-column or 4-column (`grid-cols-2`, `xl:grid-cols-4`), gap 12px

### Badge

Status pills with icon support and semantic color variants.

| Variant | Background | Text |
|---------|------------|------|
| `primary` | `--surface-blue-light` | `--primary` |
| `success` | `--success-surface` | `--success-text` |
| `neutral` | `--secondary` | `--secondary-foreground` |
| `positive` | `--positive-surface` | `--positive` |
| `destructive` | `--destructive` at 10% opacity | `--destructive` |

| Size | Padding | Font |
|------|---------|------|
| `sm` | px-2, py-0.5 | 11px (`text-2xs`) |
| `md` | px-3, py-1.5 | 12px (`text-xs`) |
| `lg` | px-4, py-2 | 12px (`text-xs`) |

Shape: `rounded-full`, semibold weight. Optional leading icon at 16px.

### Avatar

Token and user avatars with image or letter fallback.

| Size | Dimensions | Image Size |
|------|------------|------------|
| `xs` | 28×28px | 16px |
| `sm` | 32×32px | 20px |
| `md` | 40×40px | 24px |
| `lg` | 48×48px | 32px |

- Shape: `rounded-full`
- Custom `bgColor` prop for token-branded backgrounds (e.g., `rgba(39,117,202,0.12)` for USDC)
- Fallback: `ReactNode` — typically a bold letter in the token's brand color

### Card

Multi-slot card component with flexible composition.

- Background: `--card` (`#ffffff` / `#282b31`)
- Text: `--card-foreground`
- Shape: `rounded-xl` (12px)
- Border: `ring-1 ring-foreground/10`
- Padding: 16px (default), 12px (`size="sm"`)
- Gap: 16px between slots (12px for small)
- Slots: `CardHeader`, `CardTitle`, `CardDescription`, `CardAction`, `CardContent`, `CardFooter`
- Footer: `border-t bg-muted/50`, rounded bottom corners

### SectionPanel

Section-level container for dashboard content.

| Variant | Shadow |
|---------|--------|
| `default` | `--shadow-card` |
| `elevated` | `--shadow-card-md` |
| `flat` | none |

| Padding | Value |
|---------|-------|
| `sm` | 16px |
| `md` | 20px |
| `lg` | 24px |
| `xl` | 24px → 32px at `sm:` breakpoint |

- Shape: `rounded-xl`, `border-border`, `bg-card`

### IconBox

Large icon containers for onboarding, hero, and feature sections.

| Variant | Background | Icon Color |
|---------|------------|------------|
| `primary` | `--primary` | `--primary-foreground` |
| `primary-soft` | `--surface-blue-dim` | `--primary` |
| `success` | `--success` | `--success-foreground` |
| `neutral` | `--secondary` | `--secondary-foreground` |
| `foreground` | `--foreground` | `--background` |

| Size | Dimensions | Corner Radius | Icon Size |
|------|------------|---------------|-----------|
| `xs` | 32×32px | 10px | 16px |
| `sm` | 40×40px | 12px | 20px |
| `md` | 64×64px | 20px | 32px |
| `lg` | 88×88px | 28px | 44px |
| `xl` | 96×96px | 28px | 48px |
| `2xl` | 122×122px | 34px | 64px |

### Chip

Selectable pill chips for filters and suggestions.

- Default: `border-border`, `bg-card`, `text-foreground`
- Selected: `border-primary`, `bg-primary/8`, `text-primary`
- Height: 32px (sm), 36px (md)
- Shape: `rounded-full`
- Font: 13px (`text-xs-plus`), medium weight

### ChatBubble

Agent chat message bubbles.

- **Incoming**: `bg-surface-blue`, `text-muted-foreground`
- **Outgoing**: `bg-primary`, `text-primary-foreground`, `--shadow-cta-sm` shadow
- Shape: `rounded-18` (18px)
- Padding: 16px
- Font: 13px (`text-xs-plus`), `leading-relaxed`

### Input

Standard text input field.

- Height: 40px
- Shape: `rounded-lg` (8px)
- Border: 1px solid `--input`
- Background: transparent
- Placeholder: `--muted-foreground`
- Focus: `border-ring`, `ring-2 ring-ring/50`
- Font: 16px (`text-base`)
- Padding: px-3

### Progress

Linear progress bar with animated fill.

| Variant | Track | Bar |
|---------|-------|-----|
| `primary` | `--primary` at 16% opacity | `--primary` |
| `success` | `--progress-track` | `--success` |

| Size | Height |
|------|--------|
| `sm` | 6px |
| `md` | 8px |

- Shape: `rounded-full`
- Animation: 420ms with `--ease-emphasis` timing function

### NavItem

Sidebar navigation items.

- Active: `bg-primary`, `text-primary-foreground`, `--shadow-nav-active`
- Inactive: `text-muted-foreground`, `hover:bg-secondary`
- Destructive: `text-destructive`, `hover:bg-destructive/8`
- Height: 44px (h-11)
- Shape: `rounded-lg`
- Icon: 16px, leading
- Font: 14px, medium weight
- Spacing: `mb-1` between items

### StepCard

Onboarding step indicators with tri-state visuals.

| State | Border | Background | Icon Container |
|-------|--------|------------|----------------|
| `completed` | `--success-border` | `--success-surface-tint` | `bg-success text-success-foreground` |
| `active` | `--info-border` | `--surface-blue` | `bg-surface-blue-dim text-primary` |
| `pending` | `--border` | `--card` | `bg-surface-blue-dim text-primary` |

- Shape: `rounded-xl`
- Icon container: 40×40px, `rounded-full`
- Completed icon overrides to checkmark
- Title: 15px (`text-sm-plus`), bold
- Detail: 13px (`text-xs-plus`), relaxed leading, `--muted-foreground`

### AssetRow

Token display row for portfolio views.

- Layout: flex, `justify-between`, `items-center`
- Padding: px-3, py-3
- Shape: `rounded-lg`
- Left: Avatar + symbol (16px semibold) + amount (14px muted)
- Right: value (16px semibold) + detail (14px medium, custom color)

### HoldingCard

Dashboard stat card for holdings.

- Shape: `rounded-20`, border, `bg-card`
- Shadow: `--shadow-card`
- Padding: 20px
- Label: 14px, `--muted-foreground`
- Amount: 24px (`text-2xl`), bold
- Suffix: 12px, `--muted-foreground`
- Value: 14px, semibold
- Change: 12px, `text-success`, semibold
- P&L: 12px, `--muted-foreground`

### TaskCard

Trading agent task cards with stats and progress.

- Shape: `rounded-18`, border
- Padding: 16px
- Title: 14px, semibold
- Subtitle: 12px, `--muted-foreground`
- Stats grid: 3-column (default) or 2-column (compact), gap 12px
- Progress: 6px track, `bg-primary/16` → `bg-primary` fill
- Actions: `border-t`, pt-4, flex with gap-2

### StatCell

Minimal label-value pair for data grids.

- Label: 11px (`text-2xs`), `--muted-foreground`
- Value: 13px (`text-xs-plus`), semibold
- Gap: mt-1 (4px) between label and value

### FeatureItem

Feature highlight rows for onboarding screens.

- Shape: `rounded-20`
- Background: `--surface-blue`
- Padding: px-4, py-3
- Icon container: 32×32px, `rounded-full`, `bg-card`, `--primary` icon, `--shadow-icon`
- Text: 14px, medium weight, `--foreground`

### ChecklistCard

Task checklist items.

- Shape: `rounded-lg`, border
- Padding: 16px
- Title: 14px, semibold
- Description: 12px, relaxed leading, `--muted-foreground`
- Optional `tone` background color prop
- Optional action slot (mt-3)

## 5. Layout Principles

### Spacing System

- **Base unit**: 8px (`--spacing: 0.5rem`)
- **Grid**: Strict 4pt sub-grid — all spacing, padding, margins, and sizes must be multiples of 4px
- **Scale**: 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 40, 48, 56, 64px

| Token | Use |
|-------|-----|
| 2–4px | Micro spacing (badge padding, label gaps) |
| 8px | Icon gaps, tight element spacing |
| 12px | Component internal gaps, grid gaps |
| 16px | Standard padding (cards, panels, sections) |
| 20px | Elevated panel padding |
| 24px | Large panel padding, section spacing |
| 32px | Section-to-section gaps on desktop |
| 48px | Major section separation |

### Grid & Container

- Max content width: `max-w-5xl` (1024px) for main content
- Max form/card width: `max-w-md` (448px) for single-column content
- Max 2-column width: `max-w-2xl` (672px) for card grids
- Page horizontal padding: 24px (`px-6`)
- Content vertical padding: 32px (`py-8`)
- Section vertical gap: 48px (`space-y-12`)

### Border Radius Scale

| Token | Value | Use |
|-------|-------|-----|
| `--radius-xs` | 4px | Micro elements |
| `--radius-sm` | 8px | Inputs, small buttons, checklist cards |
| `--radius-10` | 10px | IconBox xs |
| `--radius-md` | 12px | Cards, section panels, step cards |
| `--radius-lg` | 16px | — |
| `--radius-18` | 18px | Chat bubbles, task cards |
| `--radius-20` | 20px | Holding cards, feature items, icon box md |
| `--radius-xl` | 24px | — |
| `--radius-28` | 28px | IconBox lg/xl |
| `--radius-2xl` | 32px | — |
| `--radius-34` | 34px | IconBox 2xl |
| `--radius-3xl` | 40px | — |
| `--radius-4xl` / `--radius-pill` | 56px | — |
| `--radius-full-pill` | 100000px | — |
| `rounded-full` | 9999px | Buttons, badges, avatars, chips, icon buttons — the signature pill shape |

### Whitespace Philosophy

- **Breathing room through surface color**: Rather than relying solely on spacing, the system uses `--surface-page` (warm off-white) as the page canvas with `--card` (pure white) cards floating above it. The color difference creates visual separation.
- **Tight within, generous between**: Components have compact internal spacing (12–16px padding) while section-to-section spacing is generous (48px). This creates dense, scannable information blocks separated by clear visual breaks.
- **Financial data density**: Portfolio views, stat grids, and trading cards pack data tightly (4–8px gaps between label/value pairs) while maintaining readability through color hierarchy (primary vs muted foreground).

## 6. Depth & Elevation

| Level | Token | Value | Use |
|-------|-------|-------|-----|
| Flat (Level 0) | — | No shadow | Page background, flat panels |
| Card (Level 1) | `--shadow-card` | `0 1px 3px rgba(17, 29, 74, 0.04), 0 1px 2px rgba(17, 29, 74, 0.06)` | Default section panels, list cards |
| Card Medium (Level 2) | `--shadow-card-md` | `0 2px 8px rgba(17, 29, 74, 0.06)` | Elevated panels, page headers |
| Card Large (Level 3) | `--shadow-card-lg` | `0 8px 24px rgba(17, 29, 74, 0.05)` | Prominent feature cards |
| Icon | `--shadow-icon` | `0 6px 20px rgba(17, 29, 74, 0.08)` | Feature item icon containers |
| CTA Small | `--shadow-cta-sm` | `0 4px 14px rgba(0, 127, 255, 0.22)` | Default primary buttons, outgoing chat bubbles |
| CTA | `--shadow-cta` | `0 8px 28px rgba(0, 127, 255, 0.28)` | Hero buttons, large icon boxes |
| CTA Large | `--shadow-cta-lg` | `0 16px 40px rgba(0, 127, 255, 0.32)` | Maximum emphasis CTAs |
| Nav Active | `--shadow-nav-active` | `0 10px 15px rgba(0, 127, 255, 0.25)` | Active sidebar navigation item |
| Dialog | `--shadow-dialog` | `0 24px 60px rgba(17, 29, 74, 0.18)` | Modal dialogs, overlays |

### Shadow Philosophy

Shadows in this system serve two distinct purposes — structural elevation and brand emphasis. Structural shadows use the foreground navy (`rgba(17, 29, 74, *)`) at very low opacities (0.04–0.08), creating barely perceptible lift that registers subconsciously. Brand shadows use the primary blue (`rgba(0, 127, 255, *)`) at higher opacities (0.22–0.32), creating a colored glow beneath interactive elements that draws attention and reinforces the brand palette.

The CTA shadow scale (sm → default → lg) allows progressive emphasis: a standard button gets a subtle blue underglow, a hero-sized button gets a dramatic one. Active navigation items share this blue shadow language, visually connecting them to the primary action palette.

## 7. Motion

| Token | Value | Use |
|-------|-------|-----|
| `--ease-emphasis` | `cubic-bezier(0.22, 1, 0.36, 1)` | Emphasized transitions — progress bars, hero animations |
| `--duration-fast` | 150ms | Micro-interactions — hover, focus |
| `--duration-normal` | 220ms | Standard transitions — color changes, opacity |
| `--duration-soft` | 420ms | Smooth transitions — progress fills, panel entries |
| `--duration-hero` | 560ms | Hero animations — page transitions, large element entries |

### Identity Gradient

The brand identity gradient animates through the brand palette for emphasis moments:

- Colors: `#007fff` → `#0038ad` → `#0d9488` → `#007fff`
- Background size: 280% for smooth looping
- Duration: 3.6s, `ease-in-out`, infinite
- Applied via `-webkit-background-clip: text` for gradient text effect
- Respects `prefers-reduced-motion`: falls back to static `--primary` color

## 8. Do's and Don'ts

### Do

- Use `--primary` (`#007fff`) for ALL interactive elements — buttons, links, focus rings, active states
- Use `--surface-page` (`#fafaf9`) as the page background, `--card` (`#ffffff`) for elevated content
- Use `rounded-full` (pill) shape for all buttons and chips — this is the signature interactive shape
- Apply `--shadow-cta-sm` to primary buttons — the blue underglow is the brand's tactile signal
- Use `--muted-foreground` for secondary text — never raw opacity on foreground color
- Build with the 8px grid — all spacing must be multiples of 4px
- Use `--font-sans` (Noto Sans Variable) for all text — hierarchy comes from size and weight, not font families
- Use `cva` (class-variance-authority) for component variants and `cn()` for class merging
- Support both light and dark themes — test every component in both modes
- Use `data-slot` attributes on component root elements for testing and styling hooks

### Don't

- Don't use raw hex values in components — always reference CSS variables or Tailwind tokens
- Don't introduce additional accent colors beyond `--primary` and `--accent` — the blue/cyan palette is the complete chromatic budget
- Don't use weight 800 or 900 — the maximum is 700 (bold), and even that is reserved for primary headings and financial numbers
- Don't use `rounded-lg` or `rounded-md` on buttons — buttons are always `rounded-full`
- Don't use `rounded-full` on cards — cards use `rounded-xl`, `rounded-18`, or `rounded-20`
- Don't add business logic, API calls, or signing logic to `packages/ui` — it is strictly a presentational component library
- Don't use React class components — functional components with hooks only
- Don't use `any` type — TypeScript strict mode is enforced
- Don't use heavy or multiple shadow layers — one shadow token per element maximum
- Don't use arbitrary spacing values (5px, 13px, 7px) — stay on the 4pt grid
- Don't place font imports in components — fonts are loaded globally via `globals.css`
- Don't mix `@alpha/ui` imports with local UI reimplementations — primitives come from the package

## 9. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Default (Mobile) | <640px | Single column, compact spacing |
| `sm:` | ≥640px | 2-column grids begin, panel padding expands |
| `md:` | ≥1024px | Full desktop layout |
| `xl:` | ≥1280px | 4-column action grids |

### Touch Targets

- Primary buttons: 40–56px height with generous horizontal padding — exceeds 48px minimum at lg/hero sizes
- Icon buttons: 32–48px square — sm (32px) approaches minimum, md/lg (40–48px) meet or exceed
- Navigation items: 44px height with full-width hit area
- Chips: 32–36px height — adequate for thumb interaction
- Action buttons: 48px height — comfortable touch target

### Collapsing Strategy

- **Mobile-first**: All default styles target mobile viewport
- **ActionBar**: 2-column at mobile, optionally 4-column at `xl:` breakpoint
- **Card grids**: single column → 2-column at `sm:` → up to 4-column at `xl:`
- **Section panels**: padding scales from 16px (sm) → 24px (md/lg) → 32px (xl) at `sm:` breakpoint
- **Typography**: hero display text should scale down proportionally on mobile while maintaining tight line-height

### Utility Classes

- `.no-scrollbar`: hides scrollbars for horizontal scroll containers (WebKit + Firefox + IE)
- `.identity-gradient`: brand gradient text effect with motion-safe animation

## 10. Agent Prompt Guide

### Quick Color Reference

- Primary CTA: `#007fff`
- Page background: `#fafaf9`
- Card surface: `#ffffff`
- Dark background: `#0a0b0d`
- Dark card surface: `#282b31`
- Heading text (light): `#111d4a`
- Heading text (dark): `#ffffff`
- Body text (secondary): `#717182` (light), `rgba(255,255,255,0.6)` (dark)
- Success: `#10b981`
- Destructive: `#d4183d`
- Focus ring: `#007fff`
- Card shadow: `0 1px 3px rgba(17,29,74,0.04), 0 1px 2px rgba(17,29,74,0.06)`
- CTA shadow: `0 4px 14px rgba(0,127,255,0.22)`

### Example Component Prompts

- "Create a primary CTA button: `rounded-full`, `bg-primary` (#007fff), `text-primary-foreground` (white), 40px height, px-5 padding, 14px Noto Sans medium weight, `shadow-[var(--shadow-cta-sm)]` blue underglow. Pill shape is mandatory."

- "Design a portfolio asset row: flex row with `justify-between`. Left side: 40px round Avatar with token color background and bold letter fallback, then symbol at 16px semibold and amount at 14px `text-muted-foreground`. Right side: value at 16px semibold and percentage at 14px in token brand color. Padding px-3 py-3, `rounded-lg`."

- "Build a balance card: `SectionPanel` with `padding='xl'`. Uppercase label at 11px semibold with 0.08em tracking in `text-muted-foreground`. Balance number at 40px bold, tight leading. Below: `Badge variant='positive'` with TrendingUp icon showing percentage, then muted dollar change. Action bar below with 4-column grid: Send (primary), Receive, Swap, Buy (all secondary)."

- "Create a trading agent task card: `rounded-18` border container, 16px padding. Header: title at 14px semibold + `Badge variant='success' size='sm'` status. Stats grid below with 3 columns showing label (11px muted) and value (13px semibold). Progress bar: 6px track, `bg-primary/16` → `bg-primary` fill. Footer actions separated by `border-t`."

- "Design an onboarding step card sequence: vertical stack of `StepCard` components with 12px gap. First two: `state='completed'` (green check icon, success surface tint, success border). Third: `state='active'` (blue surface, info border). Fourth: `state='pending'` (card surface, default border). Each has 40px round icon container, 15px bold label, 13px relaxed muted description."

- "Build a dark mode dashboard section: `bg-[#0a0b0d]` page background. Cards use `bg-[#282b31]` surface. Text: white for headings, `rgba(255,255,255,0.6)` for secondary. Borders: `rgba(255,255,255,0.1)`. Primary blue (#007fff) CTA shadow glows more prominently against dark surfaces."

### Iteration Guide

1. Every interactive element uses Primary Blue (`#007fff`) — no other accent colors for CTAs or focus
2. Page surface is warm off-white (`#fafaf9`), cards are pure white (`#ffffff`) — the contrast creates implicit elevation
3. All buttons are pill-shaped (`rounded-full`) — this is non-negotiable for the brand identity
4. Financial numbers use bold (700) weight at large sizes; secondary data uses semibold (600) at smaller sizes
5. Shadows bifurcate: structural shadows use navy tint, interactive shadows use blue tint
6. Dark mode inverts surfaces but keeps `--primary` unchanged — brand blue is constant across themes
7. Component variants use `class-variance-authority` (cva) — extend the variant system rather than adding ad-hoc styles
8. The 4pt grid is law — if a spacing value is not a multiple of 4, it is wrong
9. Noto Sans Variable is the only typeface — hierarchy through size (11–40px) and weight (400–700), never through font-family changes
10. Use `data-slot` attributes on all component root elements — they enable testing and parent-context styling
