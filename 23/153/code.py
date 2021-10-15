def f(start, x):
    if start < x: return 0
    if start == x: return 1
    return f(start - 8, x) + f(start // 2, x)

print(f(102, 43) * f(43, 5))