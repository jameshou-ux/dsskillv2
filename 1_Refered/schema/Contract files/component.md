# Component Contract Sample

## Structure

This file defines component contracts that can be used by:

- AI-first frontend generation
- Figma-first MCP workflows
- Code Connect mapping and maintenance

Each component contract should keep the same names across:

- `component.md`
- Figma component set
- code component
- Code Connect mapping

## Current Condition

This file is a sample contract document that establishes:

- a recommended schema for component definitions
- naming alignment rules
- semantic token binding guidance
- sync metadata for Figma and code

## Recommended Next Move

- use this structure as the baseline for new component contracts
- normalize component, variant, and anatomy names to this format
- add Figma node references and code paths as components become official
- keep token bindings semantic-first for colors and text roles

---

## Naming Rules

- Component names should be short, stable, and reusable.
- Variant property names must be identical in docs, Figma, code, and Code Connect.
- Anatomy names should describe function, not appearance.
- Prefer semantic names such as `label`, `supporting-text`, `leading-icon`, `container`.
- Avoid ambiguous names such as `Frame 12`, `Text 4`, `left thing`, `blue button`.

## Binding Rules

- Bind color, text, fill, stroke, surface, and elevation to semantic variables where possible.
- Bind spacing, radius, and size to primitive scales unless a semantic alias is intentionally defined.
- Keep display strings as editable content, not token definitions.
- Use semantic bindings to communicate role, not raw values.

---

## Component: Button

### Meta

- Status: sample
- Owner: design-system
- Last updated: 2026-04-06
- Figma component set: `Button`
- Figma node id: `TBD`
- Code component: `Button`
- Code file: `TBD`
- Code Connect status: pending

### Purpose

Primary action trigger used in forms, dialogs, onboarding flows, and page-level calls to action.

### Use Cases

- submit form
- continue flow
- confirm modal action
- open secondary action path

### Anatomy

- `container`
- `label`
- `leading-icon`
- `trailing-icon`
- `loading-indicator`

### Variants

- `tone`: `primary | secondary | ghost | destructive`
- `size`: `sm | md | lg`
- `width`: `auto | full`
- `icon`: `none | leading | trailing | icon-only`

### States

- `default`
- `hover`
- `pressed`
- `focus`
- `disabled`
- `loading`

### Slots

- `label`: short action text
- `leading-icon`: optional
- `trailing-icon`: optional
- `aria-label`: required when `icon=icon-only`

### Behavior Rules

- `loading` keeps the same width as the resting state
- `disabled` removes hover and pressed feedback
- `icon-only` uses square sizing and requires accessible labeling
- `full` width stretches to the parent container width

### Semantic Bindings

#### Primary

- `container.background`: `semantic.fill.primary`
- `container.border`: `semantic.border.default`
- `label.color`: `semantic.text.onPrimary`
- `icon.color`: `semantic.text.onPrimary`

#### Secondary

- `container.background`: `semantic.fill.secondary`
- `container.border`: `semantic.border.default`
- `label.color`: `semantic.text.primary`
- `icon.color`: `semantic.text.primary`

#### Ghost

- `container.background`: `semantic.fill.tertiary`
- `container.border`: `semantic.border.default`
- `label.color`: `semantic.text.action`
- `icon.color`: `semantic.text.action`

#### Destructive

- `container.background`: `semantic.fill.danger`
- `container.border`: `semantic.border.default`
- `label.color`: `semantic.text.onDanger`
- `icon.color`: `semantic.text.onDanger`

### Layout Bindings

- `height.sm`: `primitive.size.40`
- `height.md`: `primitive.size.48`
- `height.lg`: `primitive.size.52`
- `paddingX.sm`: `primitive.spacing.12`
- `paddingX.md`: `primitive.spacing.16`
- `paddingX.lg`: `primitive.spacing.20`
- `gap.iconLabel`: `primitive.spacing.8`
- `radius`: `primitive.radius.md`

### Typography

- `label.textStyle`: `semantic.typography.button`

If semantic typography aliases are not yet defined, document the current fallback here and replace later.

### Accessibility

- minimum touch target: `44px`
- visible focus treatment required
- disabled state must still meet readable contrast expectations
- icon-only variant must expose accessible name
- loading state should announce progress where relevant

### Responsive Notes

- `full` width is preferred in narrow mobile layouts
- `auto` width is preferred in dense desktop action clusters
- avoid side-by-side button groups that compress below readable label width

### Figma Requirements

- component set name must be `Button`
- variant property names must exactly match the contract
- master component layer names must use the anatomy names above
- visual properties should be bound to variables, not hardcoded values
- demo copy in masters should remain generic and replaceable

### Code Requirements

- code props should use the same variant names where possible
- visual styling must consume tokenized values instead of hardcoded literals
- state handling should match documented behavior rules
- avoid adding undocumented variants in code

### Code Connect Mapping Notes

- preferred mapping target: component set `Button`
- map to code component: `Button`
- keep variant names aligned with props for easier inspection and automation

### Drift Checklist

- does Figma still expose the same variant properties and values
- do layer names still match the documented anatomy
- do bindings still point to the intended semantic roles
- does code still expose the same public API
- has any new state or variant been added without updating this contract

---

## Suggested Next Components

- `Input`
- `TokenListItem`
- `Modal`
- `Tag`
- `SectionHeader`

