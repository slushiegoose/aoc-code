with open("input.txt") as file:
    top, bottom = (int(x) for x in file.read().split("-"))


def check_sort(x):
    y = list(str(x))
    z = sorted(y)
    return y == z

def check_double(o):
    double = False
    z = str(o)
    for x in range(1,10):
        y = z.count(str(x))
        if y == 2:
            double = True
    return double
    



z=0
for x in range(top, bottom+1):
    if check_sort(x) and check_double(x):
        z+=1
        print(x, "True")
    else: print(x, "False")

print(z)

