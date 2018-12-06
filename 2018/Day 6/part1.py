
# with open("test.txt","r") as f: inputt = f.readlines()
with open("Day 6.txt","r") as f: inputt = f.read().strip()

coordinates = list(map(lambda x: [int(y) for y in x.split(", ")],inputt))

dictie = {}

def f_closest_cord(coord):
    tempDict = {}
    for c in coordinates:
        distance = abs(c[0]-coord[0]) + abs(c[1]-coord[1])
        string = "({},{})".format(c[0],c[1])
        tempDict[string] = distance
    maximum = min(tempDict.values())
    maxie = [x for x in tempDict if tempDict[x] == maximum]
    if len(maxie) == 1:
        return maxie[0]
    return None

for x in range(0,300):
    for y in range(0, 300):
        # print(x,y)
        i = f_closest_cord([x,y])
        if i:
            if x in (1,300) or y in (1,300):
                dictie[i] = 0
            elif i in dictie and dictie[i] != 0:
                dictie[i]+=1
            elif i not in dictie:
                dictie[i] = 1

print(max(dictie.values()))

