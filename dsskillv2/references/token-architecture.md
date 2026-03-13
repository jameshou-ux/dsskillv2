# Token Architecture

Use this reference for token taxonomy, source-of-truth decisions, and architecture documentation updates.

## Core model

- The token system should use a single source of truth model.
- A common canonical source file is `source/tokens.json`, but first confirm the actual project path.
- Downstream systems consume adapted outputs; they are not the design authority.

## Token views

The PRD defines four token views:

- `primitive`
- `semantic`
- `pattern`
- `component`

These are organizational views over one system, not a strict bottom-to-top pipeline.

## Intended meaning

- `primitive`: foundational visual scales such as color, spacing, radius, and shadow.
- `semantic`: UI-role meaning such as text, background, border, and icon usage.
- `pattern`: reusable structure or composition patterns such as surfaces, layout shells, or recurring information arrangements.
- `component`: concrete component bindings for variants, states, and final consumable properties.

## Important relationship rules

- `semantic` commonly references `primitive`.
- `pattern` and `component` are peers.
- `pattern` and `component` should prefer `semantic.*` for role-based styling.
- `pattern` and `component` may directly reference `primitive.*` for structural values such as spacing, radius, size, and shadow.
- `component` answers: "what does this component variant/state use?"
- `semantic` answers: "what role does this UI value represent?"

## Architecture flow

Preferred system direction:

1. Edit `source/tokens.json`
2. Resolve references and validate schema
3. Build adapters for consumers
4. Sync outputs to Figma, runtime, or AI-facing formats

## Documentation rules

- Keep language aligned with the project's token PRD or architecture doc.
- Do not describe Figma as the source of truth.
- Do not replace the four-view model with a simplified but inaccurate hierarchy.
- Avoid absolute local links in markdown meant for GitHub or GitHub Pages.
