def contains_a_digit(s):
    return any(ch.isdigit() for ch in s)


def contains_a_alpha(s: str):
    return any(map(str.isalpha, s))


SPECIAL_CHARS = "!?#@_><;:$%&/|\\()[]{}"


def contains_a_special(s):
    return any(ch in SPECIAL_CHARS for ch in s)


def is_good_password(s):
    return len(s) > 7 and contains_a_alpha(s) and contains_a_digit(s)


def is_good_admin_password(s: str):
    return len(s) > 10 and contains_a_alpha(s) and contains_a_digit(s) and contains_a_special(s) and (
                s[-1] in SPECIAL_CHARS or s[-1].isdigit())
