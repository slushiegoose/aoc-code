# with open("Day 17.txt","r") as f: inputt = f.readlines()
with open("example.txt","r") as f: inputt=f.readlines()

x=0
y=0
clay = set()


for z in inputt:
        if "x" in z.split(",")[0]:
            # print(z)
            x = int(z[2:].split(",")[0])
            y1 = int(z.split("y=")[1].split(".")[0])
            y2 = int(z.split("..")[1])
            for p in range(y1,y2+1):
                clay.add((x,p))
        else:
            # print(z)
            y = int(z[2:].split(",")[0])
            x1 = int(z.split("x=")[1].split(".")[0])
            x2 = int(z.split("..")[1])
            for p in range(x1,x2+1):
                clay.add((p,y))

minX = min((500,min(clay, key=lambda x:x[0])[0]))
maxX = max((500,max(clay, key=lambda x:x[0])[0]))
minY = min((0,min(clay, key=lambda x:x[1])[1])) -1
maxY = max((0,max(clay, key=lambda x:x[1])[1])) +1

listie = []

for y in range(minY,maxY+1):
    l = []
    for x  in range(minX,maxX+1):
        if (x,y) == (500,0):
            l.append("+")
        elif (x,y) in clay:
            l.append("#")
        else:
            l.append(".")
    listie.append(l)
# print(clay)
# print("\n".join(["".join(x) for x in listie]))
grid = listie
wcs = ((500,0))
surface = False

# print(listie)
# print((500-minx,),(0-miny))
# print(listie[0-miny][500-minx])



toVisit = [(1,500)]
i = 0
j = 500
while len(toVisit)>0:
    n = toVisit.pop(0)
    if grid[n[0]][n[1]-minY] == '.':
        grid[n[0]][n[1]-minY] = '|'
    if n[0] == maxX:
        continue
    if grid[n[0]+1][n[1]-minY] == '.':
        toVisit.append((n[0]+1,n[1]))
        continue
    elif grid[n[0]+1][n[1]-minY] in ['~','#']:
        if grid[n[0]][n[1]-minY+1] == '.':
            toVisit.append((n[0],n[1]+1))
        if grid[n[0]][n[1]-minY-1] == '.':
            toVisit.append((n[0],n[1]-1))
        if grid[n[0]][n[1]-minY+1] in ['|','#'] and grid[n[0]][n[1]-minY-1] in ['|','#']:
            flag = True
            tmp = n[1]
            while grid[n[0]][tmp-minY+1] in ['|','~']:
                tmp += 1
            if grid[n[0]][tmp-minY+1] != '#':
                continue
            tmp = n[1]
            while grid[n[0]][tmp-minY-1] in ['|','~']:
                tmp -= 1
            if grid[n[0]][tmp-minY-1] != '#':
                continue
            tmp = n[1]
            grid[n[0]][tmp-minY] = '~'
            if grid[n[0]-1][tmp-minY] == '|':
                toVisit.append((n[0]-1,tmp))
            while grid[n[0]][tmp-minY+1] in ['|','~']:
                grid[n[0]][tmp-minY+1] = '~'
                tmp += 1
                if grid[n[0]-1][tmp-minY] == '|':
                    toVisit.append((n[0]-1,tmp))
            while grid[n[0]][tmp-minY-1] in ['|','~']:
                grid[n[0]][tmp-minY-1] = '~'
                tmp -= 1
                if grid[n[0]-1][tmp-minY] == '|':
                    toVisit.append((n[0]-1,tmp))
tildeCounter = 0
waterCounter = 0
for i in range(minX,maxX+1):
    for j in range(len(grid[i])):
        if grid[i][j] == '~':
            tildeCounter += 1
        if grid[i][j] == '|':
            waterCounter += 1
print(tildeCounter+waterCounter)
print(tildeCounter)
        
