with open("Day 7.txt","r") as f: inputt = f.readlines()
# with open("example.txt","r") as f: inputt = f.readlines()

data = []
for x in inputt:
    data.append([
        x.split("Step ")[1].split(" ")[0],
        x.split("step ")[1].split(" ")[0]])

done = set()

class Worker():
    def __init__(self, id):
        self.doing = None
        self.time = "Waiting"
        self.id = id

    def do(self, step):
        self.doing = step.letter
        self.time = step.time_taken

    def __repr__(self):
        return "<Worker {0.id} doing {0.doing} with {0.time} seconds left>".format(self)

class Step():
    def __init__(self, letter):
        self.letter = letter
        self.time_taken = ord(letter) - ord("A") + 61
        self.criteria = [x[0] for x in data if x[1] == self.letter]
        self.criteria = set(self.criteria)

    @property
    def available(self):
        return self.criteria.issubset(done) and self.letter not in done

    def __str__(self):
        return self.letter
    
    def __repr__(self):
        return self.letter

    
def wdone(worker):
    done.add(worker.doing)
    if len(done)==26: return "DONE"
    worker.doing = None
    worker.time = "Waiting"
    available = [s for s in steps if s.available]
    available.sort(key=lambda x:x.letter)
    print(available)
    iw = [w.doing for w in workers if w.doing]
    print("IW:",iw)
    av = [s for s in available if s.letter not in iw]
    print("AV:",av)
    free = [w for w in workers if w.doing is None]
    for y in av:
        free[0].do(y)
        print(free[0])
        free.pop(0)
        if not free: return


    

steps = []
for x in "ABCDEFGHIJKLMNOPQRSTUVWYXZ":
    steps.append(Step(x))

workers = []
for x in range(0,5):
    workers.append(Worker(x))

available = [s for s in steps if s.available]
print(available)
for x,y in enumerate(available):
    workers[x].do(y)

print(workers)
# quit()

secs = 0
unsolved = True
while unsolved:
    secs += 1
    for w in workers:
        if w.doing:
            w.time-=1
            if not w.time:
                x = wdone(w)
                if x:
                    secs += 1
                    unsolved = False
                    break
print(secs)