numbers = []
for n in range(286564, 287270 + 1):
    divs = []
    for i in reversed(range(1, n+1)):
        if n % i == 0:
            divs.append(i)
    numbers.append(divs)
number = []
for i in numbers:
    if len(i) >= len(number):
        number = i.copy()
print(len(number), *number[:2])