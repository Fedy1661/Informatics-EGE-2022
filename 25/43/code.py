place = 0
for i in range(154_7341, 154_7409):
    divs = 0
    for d in range(1, i+1):
        if i % d == 0:
            divs += 1
    if divs == 2:
        place += 1
        print(place, i)