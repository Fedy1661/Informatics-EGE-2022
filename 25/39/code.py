numbers = []
for i in range(573213, 575340 + 1):
    divs = []
    for d in range(1, i + 1):
        if i % d == 0:
            divs.append(d)
    if len(divs) == 4:
        numbers.append(divs)

minimal = numbers[0]

for i in numbers[1:]:
    if sum(i) < sum(minimal):
        minimal = i.copy()

print(sum(minimal), minimal[-2])