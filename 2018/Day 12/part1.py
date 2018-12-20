with open("Day 12.txt","r") as f: inputt = f.readlines()

data = inputt[0].strip("initial state: ").strip()
# print(data)
# exit()

combinations = {}

for x in inputt[2:]:
    y = x.split(" ")[0].strip()
    z = x.split(" ")[2].strip()
    combinations[y] = z

def summie(x,dictionary):
    totale = 0
    miin = min(dictionary.keys())
    maax = max(dictionary.keys())
    for x in range(miin,maax):
        if dictionary[x] == "#":
            # print(x)
            totale+=(x)
    print(_,totale)

dictie = {}

for x,y in enumerate(data):
    dictie[x] = y

for x in range(len(dictie),len(dictie)+10):
    dictie[x] = "."

for x in range(-10, 0):
    dictie[x] = "."

# print(dictie)
a = {i: dictie[i] for i in sorted(dictie.keys())}
# print(a);exit()

def p_data(y,dictionary,miin,maax):
    listie = []
    for x in range(miin,maax):
        listie.append(dictionary[x])
    print(y,"".join(listie))

no_change = False
for _ in range(0, 100):
    new_dict = {}
    miin = min(dictie.keys())
    maax = max(dictie.keys())
    # p_data(_,dictie,miin,maax)
    # print(miin,maax)
    new_dict[miin] = "."
    new_dict[miin+1] = "."
    # new_dict[miin-1] = "."
    new_dict[maax] = "."
    new_dict[maax-1] = "."
    new_dict[maax+1] = "."
    dictie[maax+1] = "."
    # dictie[miin-1] = "."
    # print(new_dict)
    for x in range(miin+2, maax):
        c = dictie[x-2] + dictie[x-1] + dictie[x] + dictie[x+1] + dictie[x+2]
        try:
            new_dict[x] = combinations[c]
        except: new_dict[x] = "."
    # print(new_dict)


    summie(_, new_dict)
    dictie = new_dict

# exit()
# print(dictie)
y = 50000000000 - 100
totale = 0
miin = min(dictie.keys())
maax = max(dictie.keys())
for x in range(miin,maax):
    if dictie[x] == "#":
        print(x)
        totale+=(x)
print(totale+(25*y))


