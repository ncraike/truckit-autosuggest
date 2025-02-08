from typing import Mapping

CATEGORIES = [
    (
        "fruit", [
            "apple",
            "avocado",
            "banana",
            "cherry",
            "grape",
            "orange",
            "pear",
            "lemon",
        ]
    ),
    (
        "vegetable", [
            "asparagus",
            "broccoli",
            "carrot",
            "potato",
            "pumpkin",
            "zucchini",
        ]
    ),
    (
        "meat", [
            "beef",
            "chicken",
            "duck",
            "fish",
            "lamb",
            "pork",
        ]
    ),
]

def build_mapping(categories_items: list[tuple[str, list[str]]]) -> Mapping[str, str]:
    mapping: Mapping[str, str] = {}
    for category, items in categories_items:
        for item in items:
            mapping[item.casefold()] = category
    return mapping


def lookup_item(mapping: Mapping[str, str], item: str) -> str | None:
    return mapping.get(item.casefold())