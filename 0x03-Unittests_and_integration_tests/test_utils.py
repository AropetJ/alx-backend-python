#!/usr/bin/env python3
"""A python3 module for testing the utils module.
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock

from utils import (access_nested_map, memoize, get_json)


class TestAccessNestedMap(unittest.TestCase):
    """
    This class contains unit tests for the function `access_nested_map`.
    It inherits from the `unittest.TestCase` class.
    """
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """
        This method tests the `access_nested_map` function.
        It uses the `parameterized.expand` decorator to run the test multiple times,
        each time with different parameters.
        Parameters:
        nested_map (Dict): The nested map to access.
        path (Tuple[str]): The path to the value in the nested map.
        expected (Union[Dict, int]): The expected result of the function.
        Returns:
        None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a"), KeyError), ({"a": 1}, ("a", "b"),
                                                   KeyError)])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception) -> None:
        """
        This method tests the `access_nested_map` function for exceptions.
        It uses the `parameterized.expand` decorator to run the test multiple
        times, each time with different parameters.
        Parameters:
        nested_map (Dict): The nested map to access.
        path (Tuple[str]): The path to the value in the nested map.
        exception (Exception): The exception that is expected to be raised.
        Returns:
        None
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class contains unit tests for the function `get_json`.
    It inherits from the `unittest.TestCase` class.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict) -> None:
        """
        This method tests the `get_json` function.
        It uses the `parameterized.expand` decorator to run the test multiple
        times, each time with different parameters.
        Parameters:
        test_url (str): The URL to get the JSON from.
        test_payload (Dict): The expected JSON payload.
        Returns:
        None
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.
    This test case verifies the functionality of the memoize decorator
    by testing the memoization of a property in the TestClass.
    """

    def test_memoize(self) -> None:
        """
        Test the memoization of a property.
        This test method creates an instance of TestClass and verifies
        that the memoization of the 'a_property' method works correctly.
        It also checks that the method is only called once.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
