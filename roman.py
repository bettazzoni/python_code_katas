symbols = (("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
           ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
           ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
           ("", "M", "MM", "MMM", "MMMM"),
           )


def roman_number(dec_value):
    return symbols[3][dec_value // 1000] + symbols[2][(dec_value % 1000) // 100] + \
            symbols[1][(dec_value % 100) // 10] + symbols[0][dec_value % 10]
