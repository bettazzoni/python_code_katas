FIRST_100_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


class PrimeNumbers:
    primes = list(FIRST_100_PRIMES)

    @classmethod
    def set_prime_list_for_testing(cls, prime_list):
        cls.primes = prime_list

    @classmethod
    def get_prime_list_for_testing(cls):
        return cls.primes

    @classmethod
    def get_prime_numbers_list_until(cls, n):
        for i in range(cls.primes[-1] + 1, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                cls.primes.append(i)
        return cls.primes


def factorize(n):
    prime_list = PrimeNumbers.get_prime_numbers_list_until(n)
    for div in prime_list:
        if n % div == 0:
            return [div] + factorize(n // div)
    return []
