numbers = {}

def f(start, x):
    if x == 5:
        numbers[start] = True
        return
    f(start + 2, x + 1), f(start + 3, x + 1), f(start * 2, x + 1)

f(10, 0)
print(len(numbers))