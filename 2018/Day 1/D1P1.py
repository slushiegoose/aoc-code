x  = 0
thingy = open("Day 1.txt","r").read()
for y in thingy.split():
    x += int(y)
print(x)


print(sum([int(x) for x in open("Day 1.txt","r").readlines()]))
