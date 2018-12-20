data = []
with open('Day 17.txt','r') as f:
    lines = f.read().split('\n')
    for line in lines:
        if line[0] == 'x':
            line = line.split(',')
            x = int(line[0].split('=')[1].strip())
            yend = int(line[1].split('..')[1].strip())
            ystart = int(line[1].split('..')[0].split('=')[1].strip())
            for y in range(ystart, yend+1):
                data.append((x,y))
        elif line[0] == 'y':
            line = line.split(',')
            x = int(line[0].split('=')[1].strip())
            yend = int(line[1].split('..')[1].strip())
            ystart = int(line[1].split('..')[0].split('=')[1].strip())
            for y in range(ystart, yend+1):
                data.append((y,x))

grid = []
minX = min(data, key=lambda x:x[1])[1]
minY = min(data, key=lambda x:x[0])[0]
maxX = max(data, key=lambda x:x[1])[1]
maxY = max(data, key=lambda x:x[0])[0]
minY -= 1
maxY += 1

for i in range(0,maxX+1):
    tmp = []
    for j in range(0,maxY-minY+1):
        tmp.append('.')
    grid.append(tmp)

grid[0][500-minY] = '+'
for i in data:
    grid[i[1]][i[0]-minY] = '#'

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

