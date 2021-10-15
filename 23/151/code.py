def numProg(start, x):
    if x < start: return 0
    if x == start: return 1
    if start % 2 == 0:
        start3 = start + 1
    else:
        start3 = start + 2
    return numProg(start + 1, x) + numProg(start * 2, x) + numProg(start3, x)

print(numProg(3, 9) * numProg(9, 17) * numProg(17, 25))
