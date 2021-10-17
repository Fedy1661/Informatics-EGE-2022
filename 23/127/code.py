def f(start, x):
    if start > x: return 0
    if start == x: return 1
    return f(start * 2, x) + f(start * 3, x)

print(f(8, 96) * f(96, 3456))