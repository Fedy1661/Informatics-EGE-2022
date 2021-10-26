numbers = []
for i in range(394480, 394540+1):
    divs = []
    for d in range(1, i + 1):
        if i % d == 0:
            divs.append(d)
    numbers.append(divs)

max_length = 0
for i in numbers:
    current_length = len(i)
    if current_length > max_length:
        max_length = current_length

for a,i in enumerate(numbers):
    if len(i) == max_length:
        i.reverse()
        print(a + 1, max_length, *i[:2])
