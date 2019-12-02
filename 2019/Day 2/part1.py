with open("input.txt") as file:
    input = [int(x) for x in file.read().split(",")]

input[1] = 12
input[2] = 2

x = 0

while True:
    function = input[x]
    one = input[x+1]
    two = input[x+2]
    store = input[x+3]
    print(x, "---", function, one, two, store)
    if function == 1:
        input[store] = input[one] + input[two]
    elif function == 2:
        input[store] = input[one] * input[two]
    elif function == 99:
        break
    x+=4

print(input)