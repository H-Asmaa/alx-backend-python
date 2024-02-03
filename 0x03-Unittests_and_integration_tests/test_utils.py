#!/usr/bin/env python3
"""
0x03. Unittests and Integration Tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """A class to test the utils.access_nested_map method"""

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

    @parameterized.expand(
        [
            ({}, ("a",), KeyError, "'a'"),
            ({"a": 1}, ("a", "b"), KeyError, "'b'"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map, path, expectedException, expectedExceptionMsg
    ):
        """A method that tests the keyError in access_nested_map
        util function"""
        with self.assertRaises(expectedException) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), expectedExceptionMsg)


class TestGetJson(unittest.TestCase):
    """A class to test utils.get_json method."""

    @patch("utils.requests.get")
    def test_get_json(self, mockGet):
        """A method that tests the return of get_json."""
        mockResponse = mockGet.return_value
        mockResponse.json.return_value = "MockedResponse"
        result = get_json("www://example.com")
        mockGet.assert_called_once_with("www://example.com")
        mockResponse.json.assert_called_once_with()
        self.assertEqual(result, "MockedResponse")


if __name__ == "__main__":
    unittest.main()
