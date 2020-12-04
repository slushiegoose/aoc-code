with open("input.txt", "r") as f:
    # input = [int(x) for x in f.readlines()]
    input = f.readlines()
    # input = f.read()
import math

input = [i.strip()*1000 for i in input]
print(input[0])

def test(start_count, start_index):
    minindex = 0
    count = start_count
    indexx = start_index
    while True:
        if len(input)-1 < indexx: break
        i = input[indexx]
        # print(count)
        if i[count] == "#":
            minindex+=1
        count+=start_count
        indexx+=start_index
    return minindex

print([test(1, 1), test(3, 1), test(5, 1), test(7, 1), test(1, 2)])

