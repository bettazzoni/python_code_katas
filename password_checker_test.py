import unittest
from password_checker import is_good_password


class PasswordCheckerTestCase(unittest.TestCase):

    def test_good_password_is_true(self):
        self.assertTrue(is_good_password("123abcDEF"))

    def test_7_char_password_is_too_short(self):
        self.assertFalse(is_good_password("12def67"))

    def test_no_digit_inside_the_password_is_false(self):
        self.assertFalse(is_good_password("abcdefghi"))

    def test_no_alfa_inside_the_password_is_false(self):
        self.assertFalse(is_good_password("12345678"))

    def test_no_alfa_and_no_digit_inside_the_password_is_false(self):
        self.assertFalse(is_good_password("èòà?!@ç|)("))


if __name__ == '__main__':
    unittest.main()
