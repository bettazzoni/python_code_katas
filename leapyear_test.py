import unittest
from leapyear import is_leap_year


class LeapYearTestCase(unittest.TestCase):

    def test_no_leap_year_BC(self):
        self.assertEqual(is_leap_year(-4), False)

    def test_0_is_not_a_leap_year(self):
        self.assertEqual(is_leap_year(0), False)

    def test_4_is_not_a_leap_year(self):
        self.assertEqual(is_leap_year(4), False)

    def test_first_leap_year_ever(self):
        self.assertEqual(is_leap_year(8), True)

    def test_leap_year_Giulian_calendar_1100(self):
        self.assertEqual(is_leap_year(1100), True)

    def test_1582_is_not_a_leap_year_in_Giulian_calendar(self):
        self.assertEqual(is_leap_year(1582), False)

    def test_first_leap_year_of_Gregorian_calendar(self):
        self.assertTrue(is_leap_year(1584))

    def test_1900_is_not_a_leap_year(self):
        self.assertFalse(is_leap_year(1900))

    def test_2000_is_an_atipical_Gregorian_leap_year(self):
        self.assertTrue(is_leap_year(2000))


if __name__ == '__main__':
    unittest.main()
