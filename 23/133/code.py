def f(start, x):
    if start < x: return 0
    if start == x: return 1
    return f(start - 1, x) + f(start >> 1, x)

print(f(int('100001', 2), int('100', 2)))