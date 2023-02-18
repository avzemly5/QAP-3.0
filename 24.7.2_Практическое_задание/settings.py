import os
from dotenv import load_dotenv

load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
empty_email = os.getenv('empty_email')
empty_password = os.getenv('empty_password')
empty_auth_key = os.getenv('empty_auth_key')
incorrect_auth_key = os.getenv('incorrect_auth_key')
