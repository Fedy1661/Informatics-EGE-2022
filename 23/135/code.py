import math

def f(start, x):
    if start > x: return 0
    if start == x: return 1
    return f(start+1, x) + f(start | 2 ** int(math.log2(start) + 1), x)

print(f(int('100', 2), int('110001', 2)))