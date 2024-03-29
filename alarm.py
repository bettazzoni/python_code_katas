import time


class Alarm:

    def __init__(self, seconds: int, time_func: callable = time.time):
        self.time_func = time_func
        self.expired_time = time_func() + float(seconds)

    def is_expired(self) -> bool:
        return self.time_func() >= self.expired_time


class AlarmWithTimeMethod:

    def __init__(self, seconds: int):
        self.expired_time = self.get_system_time() + float(seconds)

    def get_system_time(self) -> float:
        return time.time()

    def is_expired(self) -> bool:
        return self.get_system_time() >= self.expired_time
