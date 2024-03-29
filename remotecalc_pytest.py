import pytest
from remotecalc import remote_calculator


@pytest.mark.parametrize("message,json_str,result", [
    ("add 3,2", '{ "Cmd":"add", "val1":3, "val2":2 }', 5),
    ("sub 5,2", '{ "Cmd":"sub", "val1":5, "val2":2 }', 3),
    ("mul 3,2", '{ "Cmd":"mul", "val1":3, "val2":2 }', 6),
    ("div 3,2", '{ "Cmd":"div", "val1":3, "val2":2 }', 1.5),
])
def test(message, json_str, result):
    assert remote_calculator(json_str) == result, message
