numbers = {}

def f(x, step):
    if step == 12:
        numbers[x] = None
        return
    f(x + 1, step + 1), f(x * 2 - 3, step + 1)

f(3, 0)
print(len(numbers))
