JULIAN_CALENDAR_ACTIVATION = 8
GREGORIAN_CALENDAR_ACTIVATION = 1582


def is_leap_year(year: int) -> bool:
    def is_year_divisible_by(divisor: int) -> bool:
        return year % divisor == 0

    return year >= JULIAN_CALENDAR_ACTIVATION and is_year_divisible_by(4) and (
            year < GREGORIAN_CALENDAR_ACTIVATION
            or (not is_year_divisible_by(100) or is_year_divisible_by(400)))
