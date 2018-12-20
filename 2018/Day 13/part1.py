
from copy import deepcopy as copy
with open("Day 13.txt","r") as f: inputt = f.read()
# with open("example.txt","r") as f: inputt = f.read()

carts = {}

x = [list(y) for y in inputt.split("\n")]
# print(x)


p = 0
for y in range(len(x)):
    for z in range(len(x[y])):
        if x[y][z] in "^v":
            # print(y,z)
            carts[p] = [0,[y,z],"|"]
            p+=1
        elif x[y][z] in "><":
            # print(y,z)
            carts[p] = [0, [y,z],"-"]
            p+=1



def crash(p,y,z):
    print("CRASH",p,y,z,x[y][z])
    # print("\n".join(["".join(y) for y in x]))

    exit()

def move(f):
    # if f > 60: return
    print(f)
    global x
    # print("\n".join(["".join(y) for y in x]))
    new_x = copy(x)
    for y in range(len(x)):
        for z in range(len(x[y])):
            # print(y,z)
            # print(x[y][z])
            if x[y][z] not in "^<>v": continue
            try:
                cn = [t for t in carts if carts[t][1] == [y,z]][0]
            except:
                # print(f,y,z)
                # print("".join(["".join(y) for y in x]))
                exit()
            # print(x[y][z])
            if x[y][z] == ">":
                if new_x[y][z+1] in "^v<>":
                    crash(x[y][z],y,z+1)
                elif x[y][z+1] == "-":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "-"
                    carts[cn][1][1]+=1
                    new_x[y][z+1] = ">"
                elif x[y][z+1] == "\\":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "\\"
                    carts[cn][1][1]+=1
                    new_x[y][z+1] = "v"
                elif x[y][z+1] == "/":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "/"
                    carts[cn][1][1]+=1
                    new_x[y][z+1] = "^"
                elif x[y][z+1] == "+":
                    num = carts[cn][0]
                    num%=3
                    order = ["^",">","v"]
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "+"
                    carts[cn][1][1]+=1
                    carts[cn][0]+=1
                    new_x[y][z+1] = order[num]


            elif x[y][z] == "<":
                if new_x[y][z-1] in "^v<>":
                    crash(x[y][z],y,z-1)
                elif x[y][z-1] == "-":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "-"
                    carts[cn][1][1]-=1
                    new_x[y][z-1] = "<"
                elif x[y][z-1] == "\\":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "\\"
                    carts[cn][1][1]-=1
                    new_x[y][z-1] = "^"
                elif x[y][z-1] == "/":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "/"
                    carts[cn][1][1]-=1
                    new_x[y][z-1] = "v"
                elif x[y][z-1] == "+":
                    num = carts[cn][0]
                    num%=3
                    order = ["v","<","^"]
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "+"
                    carts[cn][1][1]-=1
                    carts[cn][0]+=1
                    new_x[y][z-1] = order[num]
            elif x[y][z] == "^":
                if new_x[y-1][z] in "^v<>":
                    crash(x[y][z],y-1,z)
                elif x[y-1][z] == "|":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "|"
                    carts[cn][1][0]-=1
                    new_x[y-1][z] = "^"
                elif x[y-1][z] == "\\":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "\\"
                    carts[cn][1][0]-=1
                    new_x[y-1][z] = "<"
                elif x[y-1][z] == "/":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "/"
                    carts[cn][1][0]-=1
                    new_x[y-1][z] = ">"
                
                elif x[y-1][z] == "+":
                    num = carts[cn][0]
                    num%=3
                    order = ["<","^",">"]
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "+"
                    carts[cn][1][0]-=1
                    carts[cn][0]+=1
                    new_x[y-1][z] = order[num]
            elif x[y][z] == "v":
                if new_x[y+1][z] in "^v<>":
                    crash(x[y][z],y+1,z)
                elif x[y+1][z] == "|":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "|"
                    carts[cn][1][0]+=1
                    new_x[y+1][z] = "v"
                elif x[y+1][z] == "\\":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "\\"
                    carts[cn][1][0]+=1
                    new_x[y+1][z] = ">"
                elif x[y+1][z] == "/":
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "/"
                    carts[cn][1][0]+=1
                    new_x[y+1][z] = "<"
                elif x[y+1][z] == "+":
                    num = carts[cn][0]
                    num%=3
                    order = [">","v","<"]
                    new_x[y][z] = carts[cn][2]
                    carts[cn][2] = "+"
                    carts[cn][1][0]+=1
                    carts[cn][0]+=1
                    new_x[y+1][z] = order[num]
            # print("\n".join(["".join(y) for y in x]))
    x = new_x
    # print("LOL")


                


f = 0
while True: move(f); f+=1