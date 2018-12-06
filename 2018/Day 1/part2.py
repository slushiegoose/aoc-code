# raise Exception("OOF")
x = 0
thingy = open("Day 1.txt","r").read()
z = set()

not_solved = True
while not_solved:
    for y in thingy.split():
        x += int(y)
        #print(x)
        if x in z:
            # print("{} - DONEEEEE!".format())
            not_solved = False
            break
        else:   
            z.add(x)
    
