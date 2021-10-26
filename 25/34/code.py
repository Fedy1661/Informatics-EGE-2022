numbers = []
for i in range(586132, 586430 + 1):
    divs = []
    for a in range(1, i + 1):
        if i % a == 0:
            divs.append(a)
    numbers.append(divs)

max_length = 0
for i in numbers:
    if len(i) > max_length:
        max_length = len(i)
numbers = list(filter(lambda x: len(x) == max_length, numbers))
numbers.sort(key = lambda x: x[-1])
print(len(numbers[0]), *list(reversed(numbers[0]))[:2])
print(len(numbers[-1]), *list(reversed(numbers[-1]))[:2])