numbers = []
for number in range(194441, 196500 + 1):
    divs = []
    for d in range(1, number + 1):
        if number % d == 0:
            divs.append(d)
    if len(divs) % 2 == 1:
        numbers.append(divs)

for index, number in enumerate(numbers):
    print(index + 1, number[-1], len(number), int(number[-1] ** 0.5))