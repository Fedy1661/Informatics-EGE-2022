import math

def f(start, x):
    if start < x: return 0
    if start == x: return 1
    if math.log2(start) % 1 == 0: return f(start - 1, x)
    return f(start - 1, x) + f(2 ** (len(format(start, 'b')) - 1), x)

print(f(int('10001', 2), int('1', 2)))
