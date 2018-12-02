inputt = open("Day 2.txt","r").readlines()


twocount = 0
threecount = 0
for x in inputt:
    listie = {}
    for y in x:
        if y in listie:
            listie[y] += 1
        else:
            listie[y] = 1
    twos = [x for x in listie if listie[x]==2]
    threes = [x for x in listie if listie[x]==3]
    if twos:
        twocount+=1
    if threes:
        threecount+=1
print(twocount * threecount)
