import json

cmd = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
    "pow": lambda a, b: pow(a, b)
}


def remote_calculator(json_str):
    js = json.loads(json_str)
    return cmd[js["Cmd"]](js["val1"], js["val2"])
