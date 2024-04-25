from password_checker import is_good_password, is_good_admin_password
import pytest


@pytest.mark.parametrize("message,password", [
    ("8 char", "12..AB78"),
    ("long unicode chars", "çàè^§ 1a    "),
])
def test_good_passwords(message, password):
    assert is_good_password(password), message


@pytest.mark.parametrize("message,password", [
    ("7char is too short", "12..f67"),
    ("no digit", "abcd$!ghi"),
    ("no Alpha", "12,,..78"),
    ("no digit or alpha", "........"),
])
def test_bad_passwords(message, password):
    assert not is_good_password(password), message


@pytest.mark.parametrize("message, password", [
    ("10 char is too short", "12..f678#!"),
    ("no digit or alpha", "........##...."),
    ("no Alpha", "12,,..78#!..."),
    ("no digit or alpha", "........##...."),
    ("no special", "A......  ....12"),
    ("no special last digit or special", "A.....12 . # ...."),
])
def test_bad_admin_passwords(message, password):
    assert not is_good_admin_password(password), message

@pytest.mark.parametrize("message,password", [
    ("11 char", "12..AB78  #"),
    ("long unicode chars", "çàè^§ !a    0"),
])
def test_good_admin_passwords(message, password):
    assert is_good_admin_password(password), message

