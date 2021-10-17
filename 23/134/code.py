def f(start, x):
    if start < x: return 0
    if start == x: return 1
    return f(start - 1, x) + f(start >> 1, x)

print(f(int('110111', 2), int('110', 2)))
