# Figma Variable Importer

Standalone Figma plugin package for importing adapted design-token payloads into local Figma Variables, paint styles, and typography text styles.

## What It Imports

This plugin imports JSON payloads that conform to [`schema/figma-adapter-spec.md`](../schema/figma-adapter-spec.md).

It is not intended to import:

- raw Figma variable exports
- arbitrary design-token JSON without adaptation
- project-specific skill metadata

## Package Contents

- `manifest.json`
- `code.js`
- `ui.html`
- `icon.png`

## Expected Input

The plugin expects:

- a required `primitive` set
- optional mode-aware sets such as `semantic/light` and `semantic/dark`
- token nodes with `$value`
- stable alias paths such as `{primitive.color.blue.500}`

## Typical Workflow

```text
source tokens -> adapt to figma adapter spec -> import JSON into plugin
```

If your source system is already clean and aligned, adaptation can be minimal. If it is inconsistent, add a normalization pass before adaptation.

## Install In Figma

1. Open Figma desktop.
2. Go to `Plugins` -> `Development` -> `Import plugin from manifest...`.
3. Choose [`figma-plugin/manifest.json`](./manifest.json).

## Import Flow

1. Open the plugin in a Figma file.
2. Paste a conforming JSON payload or select a JSON file.
3. Run import.
4. Review any unsupported token warnings shown by the plugin.

## Compatibility

The plugin uses the Figma Variables API and creates or updates:

- variable collections
- collection modes
- local variables
- local paint styles for gradients
- local text styles for composite typography tokens

## Typography Import Behavior

Typography is imported in two different ways:

- composite `$type: "typography"` tokens are imported as Figma text styles
- standalone font-scale tokens such as `fontFamilies`, `fontWeights`, `fontSizes`, `lineHeights`, and `letterSpacing` are treated as supporting inputs for typography resolution and are not imported as Figma variables

Example:

```json
{
  "semantic/light": {
    "textStyle": {
      "body": {
        "$type": "typography",
        "$value": {
          "fontFamily": "{primitive.typography.family.sans}",
          "fontWeight": "{primitive.typography.weight.regular}",
          "fontSize": "{primitive.typography.size.md}",
          "lineHeight": "{primitive.typography.lineHeight.md}",
          "letterSpacing": "0"
        }
      }
    }
  }
}
```

With multiple modes, text style names are created as:

- `Collection/Light/...`
- `Collection/Dark/...`
