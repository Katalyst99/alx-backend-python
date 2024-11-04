#!/usr/bin/env python3
"""The module for testing client"""
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {'key': "my_license"}}, "my_license", True),
        ({"license": {'key': "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Method to unit-test GithubOrgClient.has_license."""
        output = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Class for Integration tests"""
        @classmethod
        def setupClass(cls):
            """
            Mock requests.get to return example payloads found in the fixtures
            """
            cls.get_patcher = patch('requests.get')
            cls.mock_get = cls.get_patcher.start()

            def get_response(url):
                if url == "https://api.github.com/orgs/test-org":
                    return Mock(**{'json.return_value': cls.org_payload})
                elif url == cls.org_payload["repos_url", ""]:
                    return Mock(**{'json.return_value': cls.repos_payload})
                return Mock(**{'json.return_value': {}})
            cls.mock_get.side_effect = get_response

        def test_public_repos(self):
            """Method to test public_repos integration"""
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos(), self.expected_repos)

        def test_public_repos_with_license(self):
            """Test public_repos integration with license"""
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos(license="apache-2.0"),
                             self.apache2_repos)

        @classmethod
        def tearDownClass(cls):
            """Stop the patcher."""
            if hasattr(cls, 'get_patcher'):
                cls.get_patcher.stop()
