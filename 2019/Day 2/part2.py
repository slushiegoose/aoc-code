with open("input.txt") as file:
    y = [int(x) for x in file.read().split(",")]

x = 0

def thisrandomthing(input):
    p = 0
    while True:
        function = input[p]
        one = input[p+1]
        two = input[p+2]
        store = input[p+3]
        print(p, "---", function, one, two, store)
        if function == 1:
            input[store] = input[one] + input[two]
        elif function == 2:
            input[store] = input[one] * input[two]
        elif function == 99:
            break
        p+=4

    return input[0]
broken = False
for x in range(99):
    for z in range(99):
        input = y.copy()
        input[1] = x
        input[2] = z
        if thisrandomthing(input) == 19690720:
            print(x, z)
            print((100*x)+z)
            broken = True
            break
    if broken: break
    