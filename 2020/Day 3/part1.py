with open("input.txt", "r") as f:
    # input = [int(x) for x in f.readlines()]
    input = f.readlines()
    # input = f.read()


input = [i.strip()*100 for i in input]
print(input[0])

index = 0
count = 3
for i in input[1:]:
    print(count)
    if i[count] == "#":
        index+=1
    count+=3

print(index)


