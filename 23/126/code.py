def f(start, x):
    if start > x: return 0
    if start == x: return 1
    return  f(start + 3, x) + f(start * 2, x)

print(f(12, 96))