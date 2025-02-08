import unittest

from autosuggest.categories import CATEGORIES, build_mapping, lookup_item


class TestCategoriesBuildMapping(unittest.TestCase):
    
    def test_build_mapping_with_empty_gives_empty_mapping(self):
        self.assertEqual(build_mapping([]), {})
    
    def test_build_mapping_with_simple_gives_mapping(self):
        result = build_mapping(
            [
                ("fruit", ["apple", "banana"]),
                ("vegetable", ["broccoli"]),
                ("meat", ["beef", "chicken"]),
            ]
        )
        self.assertEqual(
            result,
            {
                "apple": "fruit",
                "banana": "fruit",
                "beef": "meat",
                "broccoli": "vegetable",
                "chicken": "meat",
            },
        )

    def test_build_mapping_with_full_gives_full_mapping(self):
        result = build_mapping(CATEGORIES)
        self.assertGreaterEqual(
            result.items(),
            {
                "banana": "fruit",
                "duck": "meat",
                "fish": "meat",
                "grape": "fruit",
                "pumpkin": "vegetable",
            }.items(),
        )
        self.assertGreaterEqual(len(result), 20)


class TestCategoriesLookupItem(unittest.TestCase):

    def setUp(self):
        self.mapping = build_mapping(CATEGORIES)

    def test_lookup_item_gives_category(self):
        self.assertEqual(
            lookup_item(self.mapping, "banana"),
            "fruit"
        )

    def test_lookup_item_mixed_case_gives_category(self):
        self.assertEqual(
            lookup_item(self.mapping, "PuMpKiN"),
            "vegetable"
        )

    def test_lookup_item_unknown_gives_none(self):
        self.assertIsNone(
            lookup_item(self.mapping, "wheat")
        )


if __name__ == "__main__":
    unittest.main()