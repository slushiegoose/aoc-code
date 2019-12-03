with open("input.txt") as file:
    wire1, wire2 = (x.split(",") for x in file.readlines())

#wire1, wire2 = (x.split(",") for x in """R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83""".split("\n"))


onelol = set()
twolol = set()

pos1 = (0, 0)
pos2 = (0, 0)

for w in wire1:
    direction = w[0]
    number = int(w[1:])

    dictionary = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    oldx, oldy = pos1
    newx, newy = dictionary[direction]

    for p in range(number):
        pos1 = (oldx + newx, oldy + newy)
        oldx, oldy = pos1
        onelol.add(pos1)
#        print(pos1)

for w in wire2:
    direction = w[0]
    number = int(w[1:])

    dictionary = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    oldx, oldy = pos2
    newx, newy = dictionary[direction]

    for p in range(number):
        pos2 = (oldx + newx, oldy + newy)
        oldx, oldy = pos2
        twolol.add(pos2)
#        print(pos2)


common =[x for x in onelol if x in twolol]

#print(common)

z = []
for x, y in common:
    distance = abs(x) + abs(y)
    z.append(distance)
print(min(z))



    

