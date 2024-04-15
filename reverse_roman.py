symbols = (("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
           ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
           ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
           ("", "M", "MM", "MMM", "MMMM","invalid","invalid", "invalid", "invalid", "invalid"),
           )


def int_from_roman(roman: str):
    roman_string= roman
    total = 0
    for j in (3, 2, 1, 0):
        for i in (9,8,7,6,5,4,3,2,1):
            s = symbols[j][i]
            if roman_string.startswith(s):
                total += pow(10, j) * i
                roman_string = roman_string[len(s):]
    return total
