def f(start, end):
    if start < end: return 0
    if start == end: return 1
    if start % 3 == 0: return f(start - 2, end)
    return f(start - 2, end) + f(start - start % 3, end)

print(f(23, 3))
