import pytest
from roman import roman_number


@pytest.mark.parametrize("decimal, roman", (
        (1, 'I'),
))
def test_roman_number(decimal: int, roman: str):
    assert roman_number(decimal) == roman


if __name__ == '__main__':
    pytest.main()
