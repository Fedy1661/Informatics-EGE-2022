numbers = {}

def f(x, step):
    if step == 15:
        numbers[x] = None
        return
    f(x * 2 + 1, step + 1), f(x + 2, step + 1)

f(2, 0)
print(len(numbers))