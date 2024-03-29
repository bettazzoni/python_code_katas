JULIAN_CALENDAR_ACTIVATION = 8
GREGORIAN_CALENDAR_ACTIVATION = 1582

def is_leap_year(year: int) -> bool:

    def is_divisible_by(dividend, divisor):
        return dividend % divisor == 0

    return year >= JULIAN_CALENDAR_ACTIVATION and is_divisible_by(year, 4) and (
            year < GREGORIAN_CALENDAR_ACTIVATION
            or (not is_divisible_by(year, 100) or is_divisible_by(year, 400)))
