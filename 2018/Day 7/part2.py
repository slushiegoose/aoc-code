with open("Day 7.txt","r") as f: inputt = f.readlines()
# with open("example.txt","r") as f: inputt = f.readlines()

data = []
for x in inputt:
    data.append([
        x.split("Step ")[1].split(" ")[0],
        x.split("step ")[1].split(" ")[0]])

order = ""
done = set()


workers = {}
secs = 0

def a(x):
    return ord(x) - ord("A") + 61

def fa():
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
    return available

def workerdone(wkr):
    done.add(workers[wkr][0])
    if len(done) == 26: print(done);return "DONE"
    workers[wkr] = []
    av = fa()
    av.sort()
    # print(av)
    print(av)
    free = [x for x in workers if workers[x] == []]
    in_workers = [y for y in workers.values() if y!=[]]
    in_workers = [y[0] for y in in_workers]
    # print(in_workers)
    av = [p for p in av if p not in in_workers]
    
    for p in av:
        workers[free[0]] = [p,a(p)]
        print(free[0],"set to",p,"at",secs)
        free.pop(0)
        if not free:return None




av = fa()
print(av)
av.sort()
workers[0] = [av[0],a(av[0])]
workers[1] = [av[1],a(av[1])]
workers[2] = [av[2],a(av[2])]
workers[3] = []
workers[4] = []
# worker[1] = []

unsolved = True
while unsolved:
    secs+=1
    # print(secs)
    for x in workers:
        if len(workers[x])==2:
            workers[x][1]-=1
            if workers[x][1] == 0:
                y = workerdone(x)
                if y:
                    unsolved = False
                    break
            
print(secs)



    




