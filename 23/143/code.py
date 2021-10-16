def f(start, x):
    if start > x: return 0
    elif start == x: return 1
    elif start == 12: return 0
    return f(start+1, x) + f(start+3, x) + f(start*2, x)

print(f(3,8) * f(8,21))