with open("input.txt", "r") as f:
    input = [int(x) for x in f.readlines()]


for i in input:
    for j in input:
        if i+j == 2020:
            print(i*j)
            quit()

