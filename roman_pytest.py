import pytest
from roman import roman_number


@pytest.mark.parametrize("decimal, roman", (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (7, 'VII'),
        (9, 'IX'),
))
def test_roman_number(decimal: int, roman: str):
    assert roman_number(decimal) == roman


if __name__ == '__main__':
    pytest.main()
