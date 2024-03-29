import unittest
from remotecalc import remote_calculator


class RemoteCalcTestCase(unittest.TestCase):
    def test_error(self):
        self.assertRaises(KeyError, remote_calculator, '{ "Cmd":"ERROR", "val1":3, "val2":2 }')

    def test_add(self):
        self.assertEqual(42, remote_calculator('{ "Cmd":"add", "val1":32, "val2":10 }'))

    def test_sub(self):
        self.assertEqual(-42, remote_calculator('{ "Cmd":"sub", "val1":10, "val2":52 }'))

    def test_mul(self):
        self.assertEqual(-88, remote_calculator('{ "Cmd":"mul", "val1":2, "val2":-44 }'))

    def test_div(self):
        self.assertEqual(-1 / 22, remote_calculator('{ "Cmd":"div", "val1":2, "val2":-44 }'))

    def test_pow(self):
        self.assertEqual(8, remote_calculator('{ "Cmd":"pow", "val1":2, "val2":3}'))


if __name__ == '__main__':
    unittest.main()
