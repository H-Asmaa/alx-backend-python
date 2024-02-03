#!/usr/bin/python3
"""
0x03. Unittests and Integration Tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A class to test the util methods"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expectedRes):
        """A method that tests access_nested_map util function."""
        self.assertEqual(access_nested_map(nested_map, path), expectedRes)


if __name__ == "__main__":
    unittest.main()
