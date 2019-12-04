with open("input.txt") as file:
    top, bottom = (int(x) for x in file.read().split("-"))


def check_sort(x):
    y = list(str(x))
    z = sorted(y)
    return y == z

def check_double(x):
    y = list(str(x))
    for i, z in enumerate(y):
        if z == y[i-1] and i!=0:
            return True
    return False

z=0
for x in range(top, bottom+1):
    if check_sort(x) and check_double(x):
        z+=1
        print(x, "True")
    print(x, "False")

print(z)

