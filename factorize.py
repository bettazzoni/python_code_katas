from typing import List

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


def list_of_primes(n):
    global PRIMES
    out_list: list[int] = list(PRIMES)
    if n > 100:
        for i in range(100, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                out_list.append(i)
    return out_list


def factorize(n):
    if n == 1:
        return [1]
    if n <= 0:
        return None
    return _factorize_core(n, list_of_primes(n))


def _factorize_core(number, prime_list):
    if number in prime_list:
        return [number]
    else:
        for div in prime_list:
            if number % div == 0:
                return [div] + _factorize_core(number // div, prime_list)
        return None
