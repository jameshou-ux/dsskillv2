import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "figma_tokens_v2.json"
SOURCE_ADAPTER_FILE = BASE_DIR / "figma_tokens_v2.json"
FILTERED_COLLECTION_PREFIXES = ("pattern/", "component/")


def build_v2_payload():
    with SOURCE_ADAPTER_FILE.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    for key in list(payload.keys()):
        if key.startswith(FILTERED_COLLECTION_PREFIXES):
            payload[key] = {}

    payload["$metadata"] = {
        **payload.get("$metadata", {}),
        "variant": "v2",
        "generatedFromAdapter": str(SOURCE_ADAPTER_FILE.relative_to(BASE_DIR.parent.parent)),
        "figmaFilter": {
            "pattern/component": "excluded",
        },
    }
    return payload


def main():
    payload = build_v2_payload()
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
