number = []
sum_number = 0
for n in range(268220, 270335+1):
    divs = []
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            divs.append(d)
            total += d
    if len(divs) <= 4 and total > sum_number:
        number = divs.copy()
        sum_number = total
print(sum_number, len(number), *number[::-1])
