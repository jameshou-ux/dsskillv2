---
name: dsskillv2
description: Work on a design token source-of-truth repository that syncs tokens to Token Studio, Figma, runtime, or AI consumers. Use this skill when the task involves canonical token sources, adapter generation, token architecture decisions, sync workflows, or token documentation.
metadata:
  short-description: Maintain a token sync source-of-truth system
---

# DSSkillV2

Use this skill when working on a design token repository that has one canonical source and multiple consumer adapters such as Token Studio, Figma, runtime, or AI-facing outputs.

## Quick Rules

- Identify the canonical source token file first. A common choice is `source/tokens.json`.
- Do not treat Figma or generated adapter files as the editable source.
- Prefer changing source tokens and then regenerating or updating downstream files intentionally.
- Keep `primitive`, `semantic`, `pattern`, and `component` as distinct views of the same system.
- When documenting or explaining architecture, align with the project's existing token PRD or architecture doc instead of inventing a new model.

## Default Workflow

1. Inspect the user request and determine whether it targets source data, adapters, docs, or process.
2. Read only the relevant reference file:
   - For architecture and token-layer decisions, read [references/token-architecture.md](references/token-architecture.md).
   - For path discovery, generated-file handling, and sync workflow, read [references/repo-workflow.md](references/repo-workflow.md).
3. Make the smallest change that preserves the SSOT model.
4. If adapter or documentation files need to stay aligned, update them in the same turn.
5. Summarize what changed, what remains generated vs. authored, and any follow-up regeneration step if it was not performed.

## Task Routing

### Source token changes

Use this path when the user asks to add, rename, delete, regroup, or explain tokens.

- Edit the canonical source token file first unless the task is explicitly about generated output only.
- Preserve theme information and token references where possible.
- Keep semantic meaning clear; do not collapse semantic tokens into raw primitive values without reason.

### Token Studio / adapter sync

Use this path when the user asks about Token Studio JSON, Figma sync, or adapter exports.

- Treat Token Studio, Figma, runtime, and AI adapter files as consumer-facing sync outputs.
- Prefer source-driven updates over hand-editing adapter files unless the user explicitly asks for an adapter-only patch.
- If you make an adapter-only fix, call out the drift risk.

### Documentation and governance

Use this path when the user asks for PRD updates, visual architecture pages, README fixes, or workflow guidance.

- Keep terminology consistent with the four-view token architecture.
- Reference project paths accurately; avoid absolute local filesystem links in docs.
- Keep governance language aligned with Git-based review and one-way sync from source to consumers.

## Default Constraints

- The canonical token source should be singular and explicitly documented.
- `pattern` and `component` are parallel views, not a forced serial stack.
- `pattern` and `component` usually consume `semantic.*`, and may directly consume `primitive.*` for structural values such as spacing, radius, or shadow.
- Git is the review boundary; token changes should remain traceable.

## When To Read More Context

- Read [references/token-architecture.md](references/token-architecture.md) before changing token taxonomy, naming, layer semantics, or architecture docs.
- Read [references/repo-workflow.md](references/repo-workflow.md) before locating source files, changing generated outputs, or deciding whether to regenerate adapters.
