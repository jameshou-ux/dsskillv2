# Design System Adapt

Design System Adapt is split into a publishable skill, a standalone Figma plugin, a public adapter contract, and optional generator tooling.

## Packages

- [`design-system-adapt/`](design-system-adapt/) contains the skill package and references for source-first adaptation workflows.
- [`figma-plugin/`](figma-plugin/) contains the standalone Figma variable importer package.
- [`schema/figma-adapter-spec.md`](schema/figma-adapter-spec.md) defines the public JSON contract the plugin consumes.
- [`tools/build-figma-adapter.py`](tools/build-figma-adapter.py) is an optional generator for producing conforming Figma adapter payloads from a canonical token source.
- [`r2d2-ds-agent/`](r2d2-ds-agent/) is the installable team skill package for governance-aware DS work.
- [`docs/agents/r2d2-ds-agent.md`](docs/agents/r2d2-ds-agent.md) is the team-default DS agent spec and skill stack entry.

## Recommended Flow

```text
canonical tokens -> normalize (optional) -> adapt -> figma adapter payload -> Figma plugin import
```

The plugin is schema-driven rather than source-format-driven. A token system does not need to match the repository's exact internal model, but it does need to be adapted into the public Figma adapter contract before import.

## Independent Publishing Boundaries

### Skill

- Folder: [`design-system-adapt/`](design-system-adapt/)
- Install guide: [`docs/INSTALL_DESIGN_SYSTEM_ADAPT.md`](docs/INSTALL_DESIGN_SYSTEM_ADAPT.md)
- Packaged zip: `docs/design-system-adapt-skill-package.zip`
- Invocation: `$design-system-adapt`

### Figma Plugin

- Folder: [`figma-plugin/`](figma-plugin/)
- Entry manifest: [`figma-plugin/manifest.json`](figma-plugin/manifest.json)
- Usage guide: [`figma-plugin/README.md`](figma-plugin/README.md)

### Public Contract

- Spec: [`schema/figma-adapter-spec.md`](schema/figma-adapter-spec.md)
- Example output: [`adapters/figma/figma_tokens_4_collections.json`](adapters/figma/figma_tokens_4_collections.json)

### Optional Tooling

- Generator: [`tools/build-figma-adapter.py`](tools/build-figma-adapter.py)
- Existing repository implementation: [`design-system-adapt/scripts/build_figma_adapter.py`](design-system-adapt/scripts/build_figma_adapter.py)

## Notes

- `adapt` is the current public module.
- `normalize` remains important for heterogeneous or inconsistent source systems.
- The standalone plugin does not depend on the skill at runtime; the main dependency is the adapter contract described in the schema spec.
