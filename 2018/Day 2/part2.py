inputt = open("Day 2.txt","r").readlines()

def section_1():
    for p in range(0, len(inputt)):
        x = inputt[p]
        for q in range(p, len(inputt)):
            y = inputt[q]
            thingy = 0
            for z in range(0, len(x)):
                if x[z] == y[z]:
                    thingy+=1
            if thingy == len(x)-1:
                return x,y

x,y = section_1()

print(x,y)
q=""
for z in range(0, len(x)):
    if x[z] == y[z]:
        q+=x[z]

print(q)