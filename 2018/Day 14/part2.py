with open("Day 14.txt","r") as f: inputt = f.read().strip()
inputt = [int(i) for i in list(inputt)]
print(inputt)
listie = [3,7]

e1 = 0
e2 = 1

def make():
    global e1, e2, listie
    item1 = listie[e1]
    item2 = listie[e2]
    summie = item1 + item2
    append = list(str(summie))
    for x in append:
        listie.append(int(x))
    e1 += 1 + item1
    e1 %= len(listie)
    e2 += 1 + item2
    e2 %= len(listie)

thingie = len(inputt) * -1

while True:
    make()
    # print(listie[-6:])
    if listie[thingie:] == inputt:
        print(len(listie)-5)
        exit()
    elif listie[thingie-1:-1] == inputt:
        print(len(listie)-6)
        exit()
    # print(listie)

# print(listie[-10:])