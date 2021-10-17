actions = [lambda x: x + 1, lambda x: x << 1, lambda x: (x << 1) + 1]

def f(start, x):
    if start > x: return 0
    if start == x: return 1
    total = 0
    for i in actions:
        total += f(i(start), x)
    return total

print(f(int('100', 2), int('11101', 2)))