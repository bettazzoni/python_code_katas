import unittest
from factorize import factorize


class FactorizeTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual([1], factorize(1))

    def test_2(self):
        self.assertEqual([2], factorize(2))

    def test_3(self):
        self.assertEqual([3], factorize(3))

    def test_4(self):
        self.assertEqual([2, 2], factorize(4))

    def test_6(self):
        self.assertEqual([2, 3], factorize(6))

    def test_9(self):
        self.assertEqual([3, 3], factorize(9))

    def test_12(self):
        self.assertEqual([2, 2, 3], factorize(12))

    def test_15(self):
        self.assertEqual([3, 5], factorize(15))

    def test_19(self):
        self.assertEqual([7, 11, 19], factorize(19 * 11 * 7))

    def test_3x3x3(self):
        self.assertEqual([3, 3, 3], factorize(27))

    def test_big_number(self):
        self.assertEqual([2, 19, 173], factorize(2 * 19 * 173))

    def test_big_big_number(self):
        self.assertEqual([31, 937], factorize(31 * 937))


if __name__ == '__main__':
    unittest.main()
