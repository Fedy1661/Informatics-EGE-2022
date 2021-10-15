def numProg(start, x):
    if x < start: return 0
    if x == start: return 1
    return numProg(start + 1, x) + numProg(start + 2, x)

path = numProg(11, 17) * numProg(17, 23) * numProg(23, 29)
path2 = numProg(11, 17) * numProg(17, 29)
path3 = numProg(11, 23) * numProg(23, 29)
print(path3 + path2 - path)