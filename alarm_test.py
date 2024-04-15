import unittest
from unittest.mock import Mock
from alarm import Alarm, AlarmWithTimeMethod


class AlarmTestCase(unittest.TestCase):

    def test_flow(self):
        mock = Mock(return_value=0.0)
        a = Alarm(10, mock)
        mock.return_value = 9.99999
        self.assertFalse(a.is_expired)
        mock.return_value = 10.0
        self.assertTrue(a.is_expired)


class _Testable_AlarmWithTimeMethod(AlarmWithTimeMethod):
    def __init__(self, seconds):
        self.return_time = 0.0
        super().__init__(seconds)

    @property
    def get_system_time(self) -> float:
        return self.return_time


class AlarmWithTimeMethodTestCase(unittest.TestCase):

    def test_flow(self):
        a = _Testable_AlarmWithTimeMethod(42)
        a.return_time = 41.99999
        self.assertFalse(a.is_expired)
        a.return_time = 42.0
        self.assertTrue(a.is_expired)


if __name__ == '__main__':
    unittest.main()
