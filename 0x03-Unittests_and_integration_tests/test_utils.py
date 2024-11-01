#!/usr/bin/env python3
"""The module for testing utils file"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """The class that inherits from unittest.TestCase. for testing get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ('http://holberton.io', {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Method to test that utils.get_json returns the expected result."""
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock) as mock_get:
            output = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(output, test_payload)
