with open("input.txt", "r") as f:
    # input = [int(x) for x in f.readlines()]
    input = f.readlines()
    # input = f.read()

count=0

for x in input:
    nums, s, password = x.split(" ")
    char = s.strip(":")
    first, second = nums.split("-")
    first, second = int(first), int(second)

    if password.count(char) in range(first, second+1):
        count+=1

print(count)


