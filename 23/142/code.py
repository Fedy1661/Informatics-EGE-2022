actions = [lambda x: x + 1, lambda x: x + 2, lambda x: x * 3]

def f(start, x):
    if start > x: return 0
    elif start == x: return 1
    elif start == 14: return 0
    total = 0
    for i in actions:
        total += f(i(start), x)
    return total

print(f(1,10) * f(10,15))

