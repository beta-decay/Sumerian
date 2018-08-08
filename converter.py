import string
digs = string.digits + string.ascii_letters

# Module to convert Cuneiform numbers to Western Arabic
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return [0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(int(x % base))
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return digits

def WesternArabicToCuneiform(n):
    b60 = int2base(int(n),60)

    for i in b60:
        tens = ['','𒌋','𒌋𒌋','']

WesternArabicToCuneiform(89)
