def f(start, x):
    if start > x: return 0
    elif start == x: return 1
    elif start == 10 or start == 15: return 0
    return f(start + 1, x) + f(start + 2, x) + f(start + 3, x)

print(f(5, 11) * f(11, 18))