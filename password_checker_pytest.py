from password_checker import is_good_password
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
