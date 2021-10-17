def f(start, x):
    if start > x: return 0
    if start == x: return 1
    return f(start + 2, x) + f(start + 3, x) + f(start * 10, x)

print(f(3, 12) * f(12, 25))