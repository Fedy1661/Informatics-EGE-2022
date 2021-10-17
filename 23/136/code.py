def f(start, x):
    if start > x: return 0
    if start == x: return 1
    binary_number = bin(start)[2:]
    binary_number = int('1' + binary_number, 2)
    return f(start+1, x) + f(binary_number, x)

print(f(int('1', 2), int('11111', 2)))