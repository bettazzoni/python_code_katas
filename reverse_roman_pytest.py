import pytest
from reverse_roman import int_from_roman


@pytest.mark.parametrize("decimal, roman", (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (7, 'VII'),
        (9, 'IX'),
        (10, "X"),
        (23, "XXIII"),
        (47, "XLVII"),
        (88, "LXXXVIII"),
        (99, "XCIX"),
        (100, "C"),
        (200, "CC"),
        (342, "CCCXLII"),
        (419, "CDXIX"),
        (888, "DCCCLXXXVIII"),
        (979, "CMLXXIX"),
        (1000, "M"),
        (2000, "MM"),
        (4963, "MMMMCMLXIII"),
))
def test_roman_number(decimal: int, roman: str):
    assert int_from_roman(roman) == decimal


if __name__ == '__main__':
    pytest.main()
