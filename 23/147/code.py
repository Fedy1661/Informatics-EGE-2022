numbers = {}

def f(x, step):
    if step == 11:
        numbers[x] = True
        return
    f(x + 1, step + 1), f(x * 2 + 1, step + 1)

f(3, 0)
print(len(numbers))