inputt = open("Day 3.txt","r").readlines()

coordinates_used = {}

for x in inputt:
    top_corner = x.split("@ ")[1].split(":")[0]
    coordinates = [int(y) for y in top_corner.split(",")]
    length = int(x.split(": ")[1].split("x")[0])
    width = int(x.split("x")[1])
    for l in range(0, length):
        for w in range(0, width):
            cos = [coordinates[0]+l,coordinates[1]+w]
            string = "({},{})".format(cos[0],cos[1])
            if string in coordinates_used:
                coordinates_used[string]+=1
            else:
                coordinates_used[string] = 1
    
thing = [x for x in coordinates_used if coordinates_used[x] > 1]
print(len(thing))