with open("input.txt") as file:
    wire1, wire2 = (x.split(",") for x in file.readlines())

#wire1, wire2 = (x.split(",") for x in """R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83""".split("\n"))


onelol = set()
twolol = set()

h = dict()
i = dict()

pos1 = (0, 0)
pos2 = (0, 0)

one = 0
two = 0

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
        one +=1
        pos1 = (oldx + newx, oldy + newy)
        oldx, oldy = pos1
        h[(oldx, oldy)] = one
        onelol.add((oldx, oldy))
#       print(pos1)

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
        two+=1
        pos2 = (oldx + newx, oldy + newy)
        oldx, oldy = pos2
        i[(oldx, oldy)] = two
        twolol.add((oldx, oldy))
#        print(pos2)


#common =[(x, y, z, a) for x, y, z in onelol if x in twolol]
# lmao = {(a, b) for a, b, c in twolol}
# common = {(x, y) for x, y, z in onelol if (x,y) in lmao}

common = {x for x in onelol if x in twolol}



#print(common)

z = []
for x, y in common:
    turnone = h[(x,y)]
    turntwo = i[(x,y)]

    turns = turnone + turntwo
    z.append(turns)
print(min(z))



    

