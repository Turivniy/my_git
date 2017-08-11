"""
------
Config
------
"""

import os

BASE_URL = 'https://api.github.com'

USERNAME = os.environ.get('USERNAME', 'login')
PASSWORD = os.environ.get('PASSWORD', 'password')
