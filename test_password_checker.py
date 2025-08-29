
from unittest import TestCase
from re import compile
from password_checker import is_valid_password

class BlackBoxTest(TestCase):
    # __lowercase_regex = compile(r'.*[a-z].*')
    # __uppercase_regex = compile(r'.*[A-Z].*')
    # __digit_regex     = compile(r'.*\d.*')
    # __length_regex    = compile(r'.{8,}')


    # def check_lenght(self, password) -> bool:
    #     return bool(self.__length_regex.match(password))

    
    # def check_digit(self, password):
    #     return bool(self.__digit_regex.match(password))


    # def check_casing(self, password):
    #     return bool(self.__uppercase_regex.match(password) 
    #         and self.__lowercase_regex.match(password))
 
        
    def password_check(self, password):
        # return bool(
        #     self.check_lenght(password)
        #     and self.check_casing(password) 
        #     and self.check_digit(password)
        #     )
        return is_valid_password(password)


    def test_valid_password(self):
        pwd = "Password109"
        self.assertTrue(self.password_check(pwd))

    def test_short_password(self):
        pwd = "Sh0rt"
        self.assertFalse(self.password_check(pwd))

    def test_no_number_password(self):
        pwd = "testPassword"
        self.assertFalse(self.password_check(pwd))

    def test_no_capital_letters(self):
        pwd = "testpassw0rd"
        self.assertFalse(self.password_check(pwd))

    def test_no_small_letters(self):
        pwd = "PASSW0RD"
        self.assertFalse(self.password_check(pwd))
