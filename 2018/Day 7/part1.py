with open("Day 7.txt","r") as f: inputt = f.readlines()

data = []
for x in inputt:
    data.append([
        x.split("Step ")[1].split(" ")[0],
        x.split("step ")[1].split(" ")[0]])

order = ""
done = set()


while True:
    available = []
    for z in "ABCDEFGHIJKLMNOPQRSTUVWYXZ":
        letter = [x[0] for x in data if x[1] == z and z]
        # print(letter)
        avail = True
        for l in letter:
            if l not in done:
                avail = False
        if avail and z not in done:
            available.append(z)
    if not available:
        break
    # print(available)
    available.sort()
    done.add(available[0])
    order+=available[0]
    print("Added "+available[0])

print(order)
