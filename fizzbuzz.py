def fizzbuzz(last=100, print_func=lambda x: print("\n".join(x))):
    return print_func(["Buzz" if (i % 5 == 0 and i % 3 != 0) else
                       "Fizz" if (i % 3 == 0 and i % 5 != 0) else
                       "FizzBuzz" if (i % 3 == 0 and i % 5 == 0) else
                       str(i) for i in range(1, last + 1)])


if __name__ == '__main__':
    fizzbuzz()
