def is_good_password(s):
    contains_a_digit: bool = any(ch.isdigit() for ch in s)
    contains_a_alpha: bool = any(map(str.isalpha, s))
    return len(s) > 7 and contains_a_alpha and contains_a_digit
