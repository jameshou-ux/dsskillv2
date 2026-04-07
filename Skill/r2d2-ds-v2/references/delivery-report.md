# Skill-Wide Delivery Report

After any substantial execution — regardless of scenario — include a delivery report in this exact format.

This is required even when the task is mostly successful. It is the user's signal that the run is complete and their entry point for the next iteration.

---

## Report Template

```
## Delivery Report

Scenario:         [DS Governance / DS To Design / Design To Demo / Prompt To Demo / DS To Code]
Confidence:       [High / Medium / Low] — [one-line concrete reason]
DS depth reached: [visual-approximation / primitive-token / semantic-token / local-component / canonical-component]
Evidence basis:   [live Figma + source token JSON / design-context bundle + source token JSON / source token JSON only / repo + Figma / other]
Agent limits:     [none / one-line note about missing capabilities that affected confidence or depth]

High-confidence areas:
- [area name]: [reason — e.g., "Button uses canonical DS library component, key imported by reference"]
- [area name]: [reason — e.g., "All color fills bound to semantic variables from Semantic collection"]

Low-confidence / approximate areas:
- [area name]: [reason — e.g., "No semantic token for nav bar border; used primitive gray.800 as Tier 4 fallback"]
- [area name]: [reason — e.g., "Transaction row pattern not in DS; built local reusable component as Tier 5 approximation"]

DS gaps found:
- [gap description]: [what was needed / what tier was used / what DS needs to fix it]
- "none" if no gaps found

Source agreement:
- Figma ↔ source token JSON:  [aligned / partial mismatch / conflict / not checked — one-line note]
- Output ↔ source token JSON: [aligned / partial mismatch / conflict / not checked — one-line note]
- Screenshot ↔ node data:     [aligned / mismatch / not checked — one-line note, only include if relevant]

Next input needed:
- [specific thing the user should provide next to get a tighter result]
- "none — run is complete" if nothing is needed
```

---

## For Figma write-back runs, also include

```
Figma output:
- Build method:       [clone-based / primitive-built / locally-componentized / library-componentized]
- Review surface:     [section link / screen link / node ID: xxxxxxx]
- Validation basis:   [metadata only / screenshot only / metadata + screenshot + node data]
```

---

## Confidence Tie-to-Facts Rule

Confidence must be backed by at least one concrete fact. Do not report a vague feeling.

Use from this list:

| Fact | Confidence effect |
|------|-------------------|
| Exact canonical component match used | High |
| Only primitive tokens available, no semantic layer | Medium or Low |
| Required Figma surface missing or not canonical | Low |
| Live Figma access unavailable but exact design-context bundle supplied | Usually Medium |
| Output built from real DS library assets | High |
| Output built from Tier 4–5 approximations | Medium or Low |
| Design brief is specific with defined states | High |
| Design brief is underspecified or missing states | Medium or Low |
| Screenshot output matches node data | Validation confirmed |
| Screenshot output does not match node data | Flag mismatch, do not guess |

---

## DS Depth Scale

Use this scale consistently across all reports and internal reasoning:

| Depth label | Meaning |
|-------------|---------|
| `canonical-component` | DS library component instance used directly |
| `local-component` | Smallest reusable local component built from DS tokens (not in library) |
| `semantic-token` | Composed from semantic tokens; no component or pattern available |
| `primitive-token` | Composed from primitive tokens; no semantic token maps the intent |
| `visual-approximation` | Tier 5 gap; built locally without DS backing; must be reported as a gap |

Report the lowest depth reached for the run as the overall `DS depth reached` value.

---

## Example Report — Prompt To Demo (Figma prototype)

```
## Delivery Report

Scenario:         Prompt To Demo
Confidence:       Medium — semantic tokens fully applied but no canonical component for transaction rows
DS depth reached: local-component (Tier 2 pattern + Tier 3 semantic tokens for most regions;
                  Tier 5 approximation for transaction row list item)
Evidence basis:   live Figma + source token JSON
Agent limits:     none

High-confidence areas:
- Primary CTA Button: canonical DS library component, imported by key
- Background fills: all screens use background/general and background/card semantic variables
- Text colors: text/primary and text/secondary semantic variables applied throughout
- Nav bar: semantic tokens for height, padding, and background applied

Low-confidence / approximate areas:
- Transaction row list item: no DS component or pattern; built as local reusable component
  using list/tokenItem spacing tokens and semantic text colors — marked as Tier 5

DS gaps found:
- Transaction row list item: DS has spacing tokens (list/tokenItem/gap, list/tokenItem/height)
  but no component definition. Recommend adding a TokenListItem component to the DS library.

Source agreement:
- Figma ↔ source token JSON:  aligned — all variable IDs match Source Token V5 semantic paths
- Output ↔ source token JSON: aligned — no raw hex values used
- Screenshot ↔ node data:     aligned — button labels and variable bindings confirmed in node data

Next input needed:
- Switch Figma to Dark mode variable collection to verify dark theme rendering
- Add TokenListItem to DS library to promote this to Tier 1 in the next run

Figma output:
- Build method:       locally-componentized (library components for buttons; local component for list items)
- Review surface:     node ID: 3437:137 (screen 1), 3437:138 (screen 2)
- Validation basis:   metadata + screenshot + node data
```
