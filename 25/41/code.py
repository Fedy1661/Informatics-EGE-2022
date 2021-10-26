numbers = []
for i in range(4_671_032, 4_671_106 + 1):
    divs = []
    for d in range(1, i + 1):
        if i % d == 0:
            divs.append(d)
    if len(divs) == 2:
        numbers.append(divs)

for a, i in enumerate(numbers):
    print(a + 1, i[-1])