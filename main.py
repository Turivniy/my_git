"""
Main
"""

import json
import requests
import config


class MyGit():
    def __init__(self, base_url, name, password):
        self.session = requests.Session()
        self.session.auth = (name, password)
        self.responce = self.session.get(base_url)

    def get_public_email_addresses(self):
        """Method to retrieve public email addresses"""
        return self.session.get(config.BASE_URL + '/user/public_emails')

    def get_email_addresses(self):
        """Method to retrieve email addresses"""
        return self.session.get(config.BASE_URL + '/user/emails')

    def add_email_address(self, emails):
        """Method to add email address(es)

        Args:
            emails (list): list of emails
        """
        return self.session.post(config.BASE_URL + '/user/emails',
                                 data=json.dumps(emails))

    def delete_email_address(self, emails):
        """Method to delete email address(es)

        Args:
            emails (list): list of emails
        """
        return self.session.delete(config.BASE_URL + '/user/emails',
                                   data=json.dumps(emails))

    def toggle_primary_email_visibility(self, emails):
        """Method to toggle email address(es) visibility

        Args:
            emails (list): list of emails
        """
        return self.session.patch(config.BASE_URL + '/user/email/visibility',
                                  data=json.dumps(emails))


if __name__ == '__main__':
    auth = MyGit()
