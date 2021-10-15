numbers = {}

def f(x, step):
    if step == 13:
        numbers[x] = True
        return
    f(x + 3, step + 1), f(x * 2 + 1, step + 1)

f(2, 0)
print(len(numbers))
