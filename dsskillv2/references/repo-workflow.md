# Workflow

Use this reference for path discovery, generated files, and common token-repository operations.

## Common paths

- `source/tokens.json`: common canonical token source path
- `adapters/tokenstudio/`: common Token Studio output path
- `adapters/figma/`: common Figma-oriented adapter path
- `prd_v1.md` or similar: common architecture/governance document
- `docs/` or project doc pages: common place for visual architecture docs

Do not assume these paths exist. Discover the actual project structure first.

## Common utility types

Token repositories often include scripts such as:

- conversion scripts
- transform or normalization scripts
- split or merge scripts
- adapter builders
- Figma push or sync utilities

Use existing scripts when they clearly fit the requested task. Otherwise, prefer direct edits plus a clear explanation of whether outputs were regenerated.

## Edit policy

- Prefer source-first edits.
- Update generated or consumer-facing outputs only when required by the task or when leaving them stale would be misleading.
- If docs mention project files, use repo-relative links.
- If GitHub Pages content is involved, ensure files exist at the published paths.

## Common task mapping

- Token naming or structure issue: locate the canonical source and project architecture doc first.
- Token Studio sync issue: locate adapter output paths after confirming the source model.
- Architecture explanation request: use the project's existing terminology and diagrams.
- README or Pages issue: check for broken relative paths and publication-path compatibility.
