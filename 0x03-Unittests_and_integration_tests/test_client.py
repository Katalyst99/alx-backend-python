#!/usr/bin/env python3
"""The module for testing client"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        """Method to unit-test GithubOrgClient._public_repos_url."""
        payload = {
            "repos_url": "https://api.github.com/users/google/repos"
        }
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value=payload
        ):
            test_class = GithubOrgClient('test')
            output = test_class._public_repos_url
            self.assertEqual(output, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mockJson):
        """
        Method to test hat the list of repos,
        is what you expect from the chosen payload.
        """
        test_payload = [
                {'name': "Facebook"},
                {'name': "Google"},
                {'name': "X"}
        ]
        mockJson.return_value = test_payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test-org/repos"
        ):
            test_class = GithubOrgClient('test')
            output = test_class.public_repos()

            reposName = ['Facebook', "Google", 'X']
            self.assertEqual(output, reposName)
            mockJson.assert_called_once_with(
                    "https://api.github.com/orgs/test-org/repos")
