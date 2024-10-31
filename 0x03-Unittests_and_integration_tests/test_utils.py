#!/usr/bin/env python3
"""The module to parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """The class that inherits from unittest.TestCase."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """Method to test that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, output):
        """Method to test that a KeyError is raised."""
        with self.assertRaises(output):
            access_nested_map(nested_map, path)
