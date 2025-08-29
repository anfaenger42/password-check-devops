
import unittest
from password_checker import is_valid_password

class TestPasswordChecker(unittest.TestCase):
    def test_valid_passwords(self):
        self.assertTrue(is_valid_password("Password1!"))
        self.assertTrue(is_valid_password("Test1234?"))
        self.assertTrue(is_valid_password("MySecure123&"))

    def test_too_short(self):
        self.assertFalse(is_valid_password("Pass1!"))
        self.assertFalse(is_valid_password("Ab1!"))

    def test_missing_number(self):
        self.assertFalse(is_valid_password("Password!"))
        self.assertFalse(is_valid_password("NoNumber!"))

    def test_missing_uppercase(self):
        self.assertFalse(is_valid_password("password1!"))
        self.assertFalse(is_valid_password("lowercase123!"))

    def test_missing_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1!"))
        self.assertFalse(is_valid_password("ALLCAPS123!"))

    def test_missing_special_character(self):
        self.assertFalse(is_valid_password("Password1"))
        self.assertFalse(is_valid_password("Password123"))

if __name__ == "__main__":
    unittest.main()
