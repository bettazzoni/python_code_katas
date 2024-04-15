import unittest
import time
from alarm import Alarm


class AlarmFunctionalTestCase(unittest.TestCase):
    def test_zero_delay(self):
        a = Alarm(0)
        self.assertTrue(a.is_expired)

    # DO NOT DO THIS! it is dangerous : in theory this can fail
    def test_at_the_start_time_is_not_expired(self):
        a = Alarm(10)
        self.assertFalse(a.is_expired)

    def test_after_sleeping_10_seconds_is_expired(self):
        a = Alarm(10)
        time.sleep(10)  # system process sleeps for N seconds
        self.assertTrue(a.is_expired)


if __name__ == '__main__':
    unittest.main()
