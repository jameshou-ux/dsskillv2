#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path("/Users/jameshou/Desktop/imToken Repos/dsskillv2 proj")
SOURCE = ROOT / "Iteration temp" / "source_token_v5.json"


def walk_tokens(obj, prefix=""):
    out = {}
    if not isinstance(obj, dict):
        return out
    for key, value in obj.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}/{key}" if prefix else key
        if isinstance(value, dict):
            if "$value" in value:
                out[path] = value
            out.update(walk_tokens(value, path))
    return out


def parse_scalar(value):
    if isinstance(value, str) and value.endswith("px"):
        return float(value[:-2]) if "." in value[:-2] else int(value[:-2])
    if isinstance(value, str) and value.endswith("%"):
        return value
    return value


def normalize_alias(value):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return value[1:-1].replace(".", "/")
    return value


def scope_for(collection, name, token_type):
    if collection == "Primitive":
        if name.startswith("color/"):
            return []
        if name.startswith("spacing/"):
            return ["GAP"]
        if name.startswith("size/"):
            return ["WIDTH_HEIGHT"]
        if name.startswith("radius/"):
            return ["CORNER_RADIUS"]
        if name.startswith("typography/family/"):
            return ["FONT_FAMILY"]
        if name.startswith("typography/weight/"):
            return ["FONT_WEIGHT"]
        if name.startswith("typography/size/"):
            return ["FONT_SIZE"]
        if name.startswith("typography/lineHeight/"):
            return ["LINE_HEIGHT"]
        if name.startswith("typography/letterSpacing/"):
            return []
    if collection == "Semantic":
        if name.startswith(("background/", "fill/", "status/")):
            return ["FRAME_FILL", "SHAPE_FILL"] if not name.startswith("status/") else ["FRAME_FILL", "SHAPE_FILL", "TEXT_FILL"]
        if name.startswith("text/"):
            return ["TEXT_FILL"]
        if name.startswith(("stroke/", "border/")):
            return ["STROKE_COLOR"]
    if collection in {"Pattern", "Component"}:
        if name.endswith(("/background", "/fieldBackground", "/icon", "/border")):
            if name.endswith("/border"):
                return ["STROKE_COLOR"]
            return ["FRAME_FILL", "SHAPE_FILL"]
        if any(name.endswith(suffix) for suffix in ("/padding", "/paddingX", "/paddingY", "/contentTopGap", "/sectionGap", "/actionGap", "/rowGap", "/gap")):
            return ["GAP"]
        if any(name.endswith(suffix) for suffix in ("/height", "/iconSize", "/closeButtonSize", "/dragHandleWidth", "/dragHandleHeight")):
            return ["WIDTH_HEIGHT"]
        if name.endswith("/radius"):
            return ["CORNER_RADIUS"]
    if token_type == "color":
        return ["FRAME_FILL", "SHAPE_FILL"]
    return []


def code_syntax_for(name):
    return f"var(--ds-{name.replace('/', '-')})"


def mode_values_for(data, collection, name, raw):
    if collection == "Primitive":
        value = parse_scalar(normalize_alias(raw))
        return {"Light": value, "Dark": value}

    def resolve(theme):
        root = data[theme][collection.lower()]
        obj = root
        for segment in name.split("/"):
            obj = obj[segment]
        return parse_scalar(normalize_alias(obj["$value"]))

    return {"Light": resolve("Light"), "Dark": resolve("Dark")}


def convert_non_typography(data, entries, collection):
    out = []
    skipped = []
    for name, token in entries.items():
        token_type = token.get("$type", "")
        raw = token.get("$value")
        desc = token.get("$description", "")
        if token_type == "gradient":
            skipped.append({"collection": collection, "name": name, "reason": "represented_as_paint_style"})
            continue
        if token_type == "typography":
            skipped.append({"collection": collection, "name": name, "reason": "represented_as_text_style"})
            continue
        if isinstance(raw, str) and raw.startswith("{semantic.font."):
            skipped.append({"collection": collection, "name": name, "reason": "represented_as_text_style_alias"})
            continue
        out.append(
            {
                "collection": collection,
                "name": name,
                "type": token_type,
                "modeValues": mode_values_for(data, collection, name, raw),
                "description": desc,
                "scopes": scope_for(collection, name, token_type),
                "codeSyntax": code_syntax_for(name),
            }
        )
    return out, skipped


def build_payload(data):
    primitive = walk_tokens(data["Primitive"])
    semantic = walk_tokens(data["Light"]["semantic"])
    pattern = walk_tokens(data["Light"]["pattern"])
    component = walk_tokens(data["Light"]["component"])

    foundation = []
    skipped = []
    for collection, entries in (
        ("Primitive", {k.replace("primitive/", "", 1): v for k, v in primitive.items()}),
        ("Semantic", semantic),
        ("Pattern", pattern),
        ("Component", component),
    ):
        converted, skipped_entries = convert_non_typography(data, entries, collection)
        foundation.extend(converted)
        skipped.extend(skipped_entries)

    text_styles = []
    for name, token in data["Light"]["semantic"]["font"].items():
        text_styles.append(
            {
                "name": name,
                "description": token.get("$description", ""),
                "value": token["$value"],
            }
        )

    gradients = []
    for mode in ("Light", "Dark"):
        for name, token in data[mode]["semantic"]["gradient"].items():
            gradients.append(
                {
                    "mode": mode,
                    "name": name,
                    "description": token.get("$description", ""),
                    "value": token["$value"],
                }
            )

    return {
        "foundationVariables": foundation,
        "textStyles": text_styles,
        "gradients": gradients,
        "skipped": skipped,
    }


def main():
    data = json.loads(SOURCE.read_text())
    payload = build_payload(data)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
