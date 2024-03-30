import pytest
from leapyear import is_leap_year

LEAP_YEAR = True


@pytest.mark.parametrize("message, year, is_leap", (
        ("No leap years BC", -4, False),
        ("Year zero ", 0, False),
        ("in 4 AC Julian Calendar was not applied", 4, False),
        ("First leap year", 8, LEAP_YEAR),
        ("1100 was a leap year", 1100, LEAP_YEAR),
        ("1582 was NOT a leap year", 1582, False),
        ("1584 was the first leap year in the Gregorian calendar", 1584, LEAP_YEAR),
        ("1900 was NOT a leap year (modified by the Gregorian calendar)", 1900, False),
        ("2000 was a leap year (modified by the Gregorian calendar)", 2000, LEAP_YEAR),
))
def test_is_leap_year(message: str, year: int, is_leap: bool):
    assert is_leap_year(year) == is_leap, message


if __name__ == '__main__':
    pytest.main()
