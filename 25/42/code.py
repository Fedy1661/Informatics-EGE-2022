place = 0
for i in range(420_2865, 420_2923+1):
    divs = 0
    for d in range(1, i+1):
        if i % d == 0:
            divs += 1
    if divs == 2:
        place +=1
        print(place, i)