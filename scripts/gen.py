import json
from pathlib import Path

NAMESPACE = "template_reforging"

OUTPUT_DIR = Path("data") / NAMESPACE / "recipe"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

rows = [
    "| Template | Base | Addition | Result |",
    "| --- | --- | --- | --- |"
]

templates = {
    "netherite_upgrade_smithing_template": "netherrack",

    "sentry_armor_trim_smithing_template": "cobblestone",
    "vex_armor_trim_smithing_template": "cobblestone",
    "wild_armor_trim_smithing_template": "mossy_cobblestone",
    "coast_armor_trim_smithing_template": "cobblestone",
    "dune_armor_trim_smithing_template": "sandstone",

    "wayfinder_armor_trim_smithing_template": "terracotta",
    "raiser_armor_trim_smithing_template": "terracotta",
    "shaper_armor_trim_smithing_template": "terracotta",
    "host_armor_trim_smithing_template": "terracotta",

    "ward_armor_trim_smithing_template": "cobbled_deepslate",
    "silence_armor_trim_smithing_template": "cobbled_deepslate",

    "tide_armor_trim_smithing_template": "prismarine",
    "snout_armor_trim_smithing_template": "blackstone",
    "rib_armor_trim_smithing_template": "netherrack",
    "eye_armor_trim_smithing_template": "end_stone",
    "spire_armor_trim_smithing_template": "purpur_block",

    "flow_armor_trim_smithing_template": "breeze_rod",
    "bolt_armor_trim_smithing_template": ["copper_block","waxed_copper_block"],
}


for template_id, material_id in templates.items():

    #recipe
    recipe = {
        "type": "smithing_transform",
        "template":  material_id,
        "base": template_id,
        "addition": "diamond",
        "result": {
            "id": template_id,
            "count": 2
        }
    }

    path = OUTPUT_DIR / f"{template_id}.json"

    with path.open("w", encoding="utf-8") as f:
        json.dump(recipe, f, indent=4, ensure_ascii=False)

    print(f"Generated: {path}")

    # md
    # if list, then separate by comma
    material_str = (
        ", ".join(material_id) 
        if isinstance(material_id, list)
        else material_id
    )

    rows.append(f"| {material_str} | {template_id} | diamond | 2x {template_id} |")

Path("recipes.md").write_text("\n".join(rows) + "\n", encoding="utf-8")