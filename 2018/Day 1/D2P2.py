x = 0
thingy = open("Day 1.txt","r").read()
z = [0]
while True:
    for y in thingy.split():
        x += int(y)
        #print(x)
        if x in z:
            print(f"{x} - DONEEEEE!")
            break
        else:   
            z.append(x)
    
