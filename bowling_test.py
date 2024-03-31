import unittest
from bowling_func import score

TESTS_DATA = (
    ("empty", 0, ()),
    ("All zeros", 0, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
    ("All ones", 20, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
    ("One Strike", 24, (10, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
    ("One Spare", 16, (5, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
    ("Quasi All Spare", 75, (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)),
    ("All Spare all 5s", 150, (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)),
    ("All Spare 0 & 10s", 100, (0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0)),
    ("Quasi perfect game", 270, (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)),
    ("Perfect game", 300, (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)),
    ("nines", 90, (9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0)),
    ("Other cases #1", 81, (6, 2, 6, 2, 2, 5, 5, 5, 0, 9, 9, 0, 6, 4, 10, 0, 0, 0, 0)),
    ("Other cases #2", 113, (6, 2, 6, 2, 2, 5, 5, 5, 0, 9, 9, 0, 6, 4, 10, 5, 2, 9, 1, 8)),
    ("Other cases #3", 89, (8, 0, 3, 0, 9, 0, 1, 3, 5, 2, 1, 4, 1, 6, 10, 2, 8, 5, 5, 1)),
    ("Other cases #4", 90, (9, 0, 4, 3, 5, 4, 6, 4, 5, 4, 4, 4, 8, 0, 7, 3, 1, 7, 4, 2)),
    ("Other cases #5", 85, (8, 2, 5, 0, 2, 6, 0, 7, 6, 3, 0, 10, 2, 5, 3, 0, 3, 2, 8, 2, 4)),
    ("Uncle Bob last", 167, (10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1)),
    ("9th frame Strike", 24, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 4)),
)


class BowlingTest(unittest.TestCase):

    def test(self):
        for message, expected, shoots in TESTS_DATA:
            with self.subTest():
                self.assertEqual(expected, score(*shoots), message)


if __name__ == '__main__':
    unittest.main()
