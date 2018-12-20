with open("Day 11.txt","r") as f: inputt = f.read().strip()
# with open("example.txt","r") as f: inputt = f.readlines()
# inputt = 42
import numpy as np
inputt = int(inputt)
listie = np.zeros((301,301))

def power(coords):
    value = 0
    rack = coords[0]+10         
    value = rack
    value *= coords[1]
    value += inputt
    value *= rack
    value = int(str(value)[-3])
    value-=5
    return value

def summie(top_left):
    o = 0
    x = top_left[0]
    y = top_left[1]
    size = top_left[2]
    for p in range(0,size):
        for q in range(0,size):
            o+= listie[x+p][y+q]
    return o


dictie = {}

checks = []
for x in range(1, 301):
    for y in range(1, 301):
        listie[x][y] = power([x,y])


# print(power([21,61]))
# quit()
for size in range(2,300):
    print(size)
    for x in range(1, 300-size):
        for y in range(1, 300-size):
            string = "({},{},{})".format(x,y,size)
            dictie[string] = summie([x,y,size])
            print(string, dictie[string])

maxie = max(dictie.values())
print([string for string in dictie if dictie[string]==maxie])
print(maxie)

