"""
Unittests
"""

import unittest

import config
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


class TestEmails(unittest.TestCase):
    def setUp(self):
        self.test_email = 'test_mail@email.com'
        self.auth = MyGit(config.BASE_URL,
                          name=config.USERNAME,
                          password=config.PASSWORD)
        self.auth.add_email_address([self.test_email])

    def test_check_email(self):
        emails = self.auth.get_email_addresses()
        emails_list = [mail['email'] for mail in emails.json()]

        self.assertEqual(200, emails.status_code)
        self.assertIn(self.test_email, emails_list)

    def test_primary_email_visibility(self):
        emails = self.auth.get_email_addresses()
        mail_visibility = [mail['visibility'] for mail in emails.json()
                           if mail['email'] == self.test_email]

        self.assertEqual(None, mail_visibility[0])

    def test_toggle_primary_email_visibility(self):
        self.auth.toggle_primary_email_visibility([self.test_email])
        emails = self.auth.get_email_addresses()
        mail_visibility = [mail['visibility'] for mail in emails.json()
                           if mail['email'] == self.test_email]

        self.assertEqual(True, mail_visibility[0])

    def tearDown(self):
        self.auth.delete_email_address([self.test_email])


if __name__ == '__main__':
    unittest.main()
