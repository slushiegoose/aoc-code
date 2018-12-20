with open("Day 10.txt","r") as f: inputt = f.readlines()

data = []


for x in inputt:
    px = int(x.split("<")[1].split(",")[0])
    py = int(x.split(", ")[1].split(">")[0])
    vx = int(x.split("<")[2].split(",")[0])
    vy = int(x.split(", ")[2].split(">")[0])
    data.append([[px,py],[vx,vy]])

def plot_points(data,s):
    max_x = max([x[0][0] for x in data])
    max_y = max([x[0][1] for x in data])
    min_x = min([x[0][0] for x in data])
    min_y = min([x[0][1] for x in data])
    datapoints = [x[0] for x in data]

    if max_x-min_x >= 100: return

    grid = [[' ' for i in range(max_x - min_x + 1)] for j in range(max_y - min_y + 1)]
    for i in datapoints:
        grid[i[1]-min_y][i[0]-min_x] = '█'
    lines = []
    for i in grid:
        line = ''.join(i)
        lines.append(line)
    print("\n".join(lines))
    print(s)
    print("\n\n\n\n\n\n\n")

s=0
while True:
    plot_points(data,s)
    for x in range(len(data)):
        data[x][0][0]+=data[x][1][0]
        data[x][0][1]+=data[x][1][1]
    s+=1
    #print(s)
        




    
    