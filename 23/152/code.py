def numProg(start, x):
    if x < start: return 0
    if x == start: return 1
    return numProg(start + 1, x) + numProg(start + 2, x)

part_1 = numProg(11, 17) * numProg(17, 29)
part_2 = numProg(11, 23) * numProg(23, 29)
part_general = numProg(11, 17) * numProg(17, 23) * numProg(23, 29)
print(part_1 + part_2 - part_general)