with open("Day 18.txt","r") as f: inputt = f.readlines()
from copy import deepcopy as copy

# with open("example.txt","r") as f: inputt = f.readlines()
data = [list(x.strip()) for x in inputt]

def find_adjacent(x,y):
    adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    adjacent = []
    for p,q in adj:
        try:
            if y+q < 0 or x+p < 0: continue
            r = data[y+q][x+p]
            adjacent.append(r)
        except IndexError:
            pass
    return adjacent

def minute():
    # print("\n".join(["".join(x) for x in data]))
    # print("\n\n\n\n\n")
    global data
    new_data = copy(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            v = data[y][x]
            a = find_adjacent(x,y)
            # print(a)
            if v == ".":
                if a.count("|") >=3:
                    new_data[y][x] = "|"
            elif v=="|":
                if a.count("#") >=3:
                    new_data[y][x] = "#"
            elif v=="#":
                if a.count("#") >=1 and a.count("|") >=1:
                    pass
                else:
                    new_data[y][x] = "."
    data = copy(new_data)
    f = "".join(["".join(x) for x in data])
    # print(f.count("|"))
    # print(f.count("#"))
    # print(f.count("|") * f.count("#"))


# print(f.count("|") * f.count("#"))
w = []
u = 0
_ = 0
while True:
    minute()
    f = "".join(["".join(x) for x in data])
    # print(f.count("|"))
    # print(f.count("#"))
    y = f.count("|") * f.count("#")
    try:
        r = w[::-1].index(y)
        if r == 27:
            u+=1
        if u == 4:
            while _ < 1000000000:
                _+=28
            _-=28
        
    except: pass
    # print(f.count("|") * f.count("#"))
    w.append(f.count("|") * f.count("#"))
    _+=1
    if _ == 1000000000:
        break

f = "".join(["".join(x) for x in data])
# print(f.count("|"))
# print(f.count("#"))


print(f.count("|") * f.count("#"))


