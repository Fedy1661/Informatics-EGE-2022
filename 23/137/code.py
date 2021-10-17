import math

def f(start, x):
    if start < x: return 0
    if start == x: return 1
    if math.log2(start) % 1 == 0: return f(start - 1, x)
    zeroize = int('1' + '0' * int(math.log2(start)), 2)
    return f(start-1, x) + f(zeroize, x)

print(f(int('1100', 2), int('100', 2)))