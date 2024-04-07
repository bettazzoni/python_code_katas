import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("message, last, ret", (
        ("first numeral", 1, ("1",)),
        ("first Fizz", 3, ("1", "2", "Fizz")),
        ("first Buzz", 5, ("1", "2", "Fizz", "4", "Buzz",)),
        ("first Buzz", 16, ("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                            "11", "Fizz", "13", "14", "FizzBuzz", "16")),
        ("first Buzz", 25, ("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
                            "Fizz", "22", "23", "Fizz", "Buzz")),
))
def test_fizzbuzz(message: str, last: int, ret: tuple):
    assert fizzbuzz(last, print_func=tuple) == ret, message


if __name__ == '__main__':
    pytest.main()
