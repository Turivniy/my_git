"""
Functional tests
"""
import unittest

import config
from main import MyGit


class TestEmailsNegative(unittest.TestCase):
    def setUp(self):
        self.auth = MyGit(config.BASE_URL,
                          name=config.USERNAME,
                          password=config.PASSWORD)

    def test_add_several_emails(self):
        test_email_1 = 'test_mail_add@email.com'
        test_email_2 = 'test_mail_add@example.com'
        self.auth.add_email_address([test_email_1, test_email_2])
        emails = self.auth.get_email_addresses()
        emails_list = [mail['email'] for mail in emails.json()]

        self.assertEqual(200, emails.status_code)
        self.assertIn(test_email_1, emails_list)
        self.assertIn(test_email_2, emails_list)

    def test_add_empty_email(self):
        test_email = ''
        self.auth.add_email_address([test_email])
        emails = self.auth.get_email_addresses()
        emails_list = [mail['email'] for mail in emails.json()]

        self.assertEqual(200, emails.status_code)
        self.assertNotIn(test_email, emails_list)

    def test_delete_several_emails(self):
        test_email_1 = 'test_mail_delete@email.com'
        test_email_2 = 'test_mail_delete@example.com'
        self.auth.add_email_address([test_email_1, test_email_2])
        emails = self.auth.get_email_addresses()
        emails_list = [mail['email'] for mail in emails.json()]

        self.auth.delete_email_address([test_email_1, test_email_2])

        self.assertEqual(200, emails.status_code)
        self.assertNotIn(test_email_1, emails_list)
        self.assertNotIn(test_email_2, emails_list)

    def test_delete_non_exist_email(self):
        test_email = 'non_exist_test_mail@email.com'
        emails = self.auth.get_email_addresses()
        emails_list = [mail['email'] for mail in emails.json()]

        self.assertEqual(200, emails.status_code)
        self.assertNotIn(test_email, emails_list)

        self.auth.delete_email_address([test_email])
        self.assertEqual(200, emails.status_code)

    def test_add_incorrect_email(self):
        test_email = '@example.com'
        self.auth.add_email_address([test_email])
        emails = self.auth.get_email_addresses()
        emails_list = [mail['email'] for mail in emails.json()]

        self.assertEqual(200, emails.status_code)
        self.assertNotIn(test_email, emails_list)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
