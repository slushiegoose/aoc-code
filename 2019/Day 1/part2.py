with open("input.txt","r") as f:
    input = [int(x) for x in f.readlines()]
    print(input)

def divide(p):
    return int(p/3)-2


summ = 0

for p in input:
    x = p
    while True:
        x = divide(x)
        if x >= 0:
            summ+=x
        else:
            break

print(summ)


