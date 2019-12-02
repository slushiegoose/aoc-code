with open("input.txt","r") as f:
    input = [int(x) for x in f.readlines()]
    print(input)


summ = 0

for p in input:
    x = int(p/3)
    x -=2
    summ+=x

print(summ)


