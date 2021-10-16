import math

def f(start, x):
    if start < x: return 0
    if start == x: return 1
    if math.log2(start) % 1 == 0: return f(start - 1, x)
    # binary_number - перевод числа из десятичной в двоичную систему исчесления
    binary_number = format(start, 'b') # OR bin(start)[2:]
    # (len(binary_number) - 1) - получаем количество цифр после единицы.
    # Например: 10000 -> 4; 1000 -> 3; 100000 -> 5;
    # Возводим в степень - 2 ** (len(binary_number) - 1)
    return f(start - 1, x) + f(2 ** (len(binary_number) - 1), x)


print(f(int('1000000', 2), int('1000', 2)))
