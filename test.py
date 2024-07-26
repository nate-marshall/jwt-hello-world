import unittest
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TestJWTAuth(unittest.TestCase):

    BASE_URL = os.getenv('BASE_URL')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    def test_login(self):
        url = f"{self.BASE_URL}/login"
        payload = {
            "username": self.USERNAME,
            "password": self.PASSWORD
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

    def test_protected_with_valid_token(self):
        login_url = f"{self.BASE_URL}/login"
        protected_url = f"{self.BASE_URL}/protected"
        
        # First, get the token
        payload = {
            "username": self.USERNAME,
            "password": self.PASSWORD
        }
        headers = {
            "Content-Type": "application/json"
        }
        login_response = requests.post(login_url, data=json.dumps(payload), headers=headers)
        token = login_response.json().get("token")
        
        # Now, access the protected route
        protected_headers = {
            "Authorization": token
        }
        protected_response = requests.get(protected_url, headers=protected_headers)
        self.assertEqual(protected_response.status_code, 200)
        self.assertIn("Welcome", protected_response.json().get("message"))

    def test_protected_with_invalid_token(self):
        url = f"{self.BASE_URL}/protected"
        headers = {
            "Authorization": "invalid_token"
        }
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 403)
        self.assertIn("Invalid token", response.json().get("message"))

    def test_protected_with_no_token(self):
        url = f"{self.BASE_URL}/protected"
        response = requests.get(url)
        self.assertEqual(response.status_code, 403)
        self.assertIn("Token is missing", response.json().get("message"))

if __name__ == "__main__":
    unittest.main()
