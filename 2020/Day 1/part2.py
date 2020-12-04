with open("input.txt", "r") as f:
    input = [int(x) for x in f.readlines()]


for i in input:
    for j in input:
        for k in input:
            if i+j+k == 2020:
                print(i*j*k)

