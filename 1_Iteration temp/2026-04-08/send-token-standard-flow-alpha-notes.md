# Standard Send Token Flow

## Structure

- Single-phone interactive prototype covering token selection, amount entry with transaction details, sign preview, and result state with toast feedback.
- One standalone HTML artifact intended for hands-on testing and iteration: `send-token-standard-flow-alpha.html`.

## Current Condition

- The prototype follows the alpha design guide directly: warm off-white page surface, pure white cards, Noto Sans typography, primary blue as the only action accent, success green reserved for confirmation, pill CTAs, and 4pt-grid spacing.
- Token selection is interactive.
- Amount entry supports live recipient editing, contact shortcuts, quick amount presets, and speed switching.
- Signature preview reflects the current prototype state before broadcast.
- Result state includes a receipt view and a replayable toast.

## Recommended Next Move

- Run a usability pass on touch targets, preset behavior, and state persistence.
- If this interaction model is approved, split the prototype into reusable send-flow components and motion specs.
