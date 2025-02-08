from typing import Mapping

CATEGORIES = [
    (
        "fruit",
        [
            "apple",
            "avocado",
            "banana",
            "cherry",
            "grape",
            "orange",
            "pear",
            "lemon",
        ],
    ),
    (
        "vegetable",
        [
            "asparagus",
            "broccoli",
            "carrot",
            "potato",
            "pumpkin",
            "zucchini",
        ],
    ),
    (
        "meat",
        [
            "beef",
            "chicken",
            "duck",
            "fish",
            "lamb",
            "pork",
        ],
    ),
]


def build_mapping(categories_items: list[tuple[str, list[str]]]) -> Mapping[str, str]:
    """Convert the CATEGORIES list to a mapping of item to category.

    Converts the CATEGORIES list above (or a similar list of categories and items)
    to a dictionary mapping each item to its category. Item names are casefolded
    for case-insensitive lookups.

    For example,

    >>> build_mapping([
    ...     ("fruit, ["apple", "banana"]),
    ...     ("vegetable, ["carrot"]),
    ...     ("meat, ["beef"]),
    ... ])
    {"apple": "fruit", "banana": "fruit", "carrot": "vegetable", "beef": "meat"}
    """
    mapping: Mapping[str, str] = {}
    for category, items in categories_items:
        for item in items:
            mapping[item.casefold()] = category
    return mapping


def lookup_item(mapping: Mapping[str, str], item: str) -> str | None:
    """Lookup an item in the given category mapping.

    Returns the item's category, or None if the item's category cannot
    be found.

    NOTE: item names are treated case-insensitive, so looking up
    "BANANA" or "Banana" will give the same result as "banana".
    """
    return mapping.get(item.casefold())
