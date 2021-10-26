numbers = []
for n in range(248015, 251575 + 1, 2):
    divs = []
    for d in range(1, n + 1):
        if n % d == 0:
            divs.append(d)
    if len(divs) % 2 == 1:
        numbers.append(divs)

for a, i in enumerate(numbers):
    print(a + 1, i[-1], len(i), int(i[-1] ** 0.5))
