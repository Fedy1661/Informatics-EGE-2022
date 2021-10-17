def f(start, x):
    if start > x: return 0
    if start == x: return 1
    if start == 43: return 0
    return f(start + 2, x) + f(start + start - 1, x) + f(start + start + 1, x)

print(f(7, 63))