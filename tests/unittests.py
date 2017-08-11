"""
Unittests
"""

import config
import unittest

from main import MyGit


class TestAuth(unittest.TestCase):
    def setUp(self):
        pass

    def test_auth_ok(self):
        auth = MyGit(config.BASE_URL,
                     name=config.USERNAME,
                     password=config.PASSWORD)
        self.assertEqual(200, auth.responce.status_code)

    def test_auth_incorrect_name(self):
        auth = MyGit(config.BASE_URL,
                     name='incorrect_name',
                     password=config.PASSWORD)
        self.assertEqual(401, auth.responce.status_code)

    def test_auth_incorrect_password(self):
        auth = MyGit(config.BASE_URL,
                     name=config.USERNAME,
                     password='incorrect_password')
        self.assertEqual(401, auth.responce.status_code)


if __name__ == '__main__':
    unittest.main()
