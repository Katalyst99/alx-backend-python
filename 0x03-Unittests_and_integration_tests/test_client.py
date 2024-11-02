#!/usr/bin/env python3
"""The module for testing client"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    The class that inherits from unittest.TestCase,
    and implements the test_org method.
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """Method test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(org)
        test_class.org()
        mock.assert_called_once_with("https://api.github.com/orgs/{}"
                                     .format(org))
