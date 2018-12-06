
with open(path + "Day 6.txt","r") as f: inputt = f.readlines()
# with open("test.txt","r") as f: inputt = f.readlines()
# inputt = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9""".split("\n")
coordinates = list(map(lambda x: [int(y) for y in x.split(", ")],inputt))
# print(coordinates)


listie = []

def f_closest_cord(coord):
    summie = 0
    for c in coordinates:
        distance = abs(c[0]-coord[0]) + abs(c[1]-coord[1])
        summie += distance
    if summie < 10000:
        return summie
    return None

for x in range(0,600):
    for y in range(0, 600):
        # print(x,y)
        i = f_closest_cord([x,y])
        if i:
            listie.append([x,y])

# print(listie)
print(len(listie))

