import pytest
from factorize import factorize, PrimeNumbers, FIRST_100_PRIMES
import random, functools

PrimeNumbers.set_prime_list_for_testing([2])


@pytest.mark.parametrize("message, expected_starting_list, all_prime_to_this_number", (
        ("Check PrimeNumbers(10)", (2, 3, 5, 7), 10),
        ("Check PrimeNumbers(20)", (2, 3, 5, 7, 11, 13, 17), 20),
        ("Check PrimeNumbers(100)", FIRST_100_PRIMES, 100),
        ("Check PrimeNumbers(200)", FIRST_100_PRIMES, 200),
))
def test_prime_number(message, expected_starting_list, all_prime_to_this_number):
    len_primes_before_test = len(PrimeNumbers.get_prime_list_for_testing())
    first_expected_element_of_result = PrimeNumbers.get_prime_numbers_list_until(all_prime_to_this_number)[
                                       :len(expected_starting_list)]
    assert tuple(expected_starting_list) == tuple(first_expected_element_of_result)
    assert len(PrimeNumbers.get_prime_list_for_testing()) > len_primes_before_test


@pytest.mark.parametrize("message, expected_primes, number_to_factorize", (
        ("Test the first prime number: 2", [2], 2),
        ("test 3", [3], 3),
        ("test 4", (2, 2), 4),
        ("test 6", (2, 3), 6),
        ("test 9", (3, 3), 9),
        ("test 12", (2, 2, 3), 12),
        ("test 15", (3, 5), 15),
        ("test 27", (3, 3, 3), 27),
        ("test 1463", (7, 11, 19), 1463),
        ("test 6574", (2, 19, 173), 6574),
        ("test 9296", (2, 2, 2, 2, 7, 83), 9296),
        ("test 45396", (2, 2, 3, 3, 97), 3492),
))
def test(message, expected_primes, number_to_factorize):
    assert set(expected_primes) == set(factorize(number_to_factorize)), message


def test_math_constraints():
    for i in range(10):
        v = random.randint(1000, 10000)  # test relatively big random numbers
        result = factorize(v)
        mult_results = functools.reduce(lambda x, y: x * y, result)
        not_prime_result = [x for x in result if not (x in PrimeNumbers.get_prime_numbers_list_until(x))]
        assert mult_results == v, (
                "Test multiply the results to have the original value.  factorize(" + str(v) + ")=" + str(result) +
                "   Multiply all elements of the list=" + str(mult_results))
        assert not_prime_result == [], (
                "Test all the results are prime numbers.     factorize(" + (str(v) + ")=" + str(result) +
                "   This results are not prime numbers=" + str(not_prime_result)))


if __name__ == '__main__':
    pytest.main()
