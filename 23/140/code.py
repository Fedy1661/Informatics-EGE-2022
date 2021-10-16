def f(start, x):
    if start > x: return 0
    if start == x: return 1
    return f(start + 2, x) + f(start + 3, x) + f(start * 4, x)

print(f(int('1', 4), int('100', 4)))
