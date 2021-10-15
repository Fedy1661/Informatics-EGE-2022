numbers = {}

def f(x):
    if x >= 100:
        return
    if x % 2 == 0:
        numbers[x] = None
    f(x+3), f(x*3)

f(3)
print(len(numbers))