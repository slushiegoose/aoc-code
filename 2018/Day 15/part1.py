with open("example.txt","r") as f: inputt = f.readlines()
    
inputt = [list(x) for x in inputt]

def reach(x, in_range):
    return in_range

def md(x, listie):
    dictie = {}
    for c in listie:
        mdistance = abs(x[0]-c[0]) + abs(x[1]-c[1])
        dictie[c] = mdistance
    y = min(dictie.values())
    if y == 1:
        return "Attack"
    n = [x for x in dictie if dictie[x] == y]
    return n

def cmd(x, c):
    return abs(x[0]-c[0]) + abs(x[1]-c[1])

def choose(a): 
    return sorted(a)[0]

def walk(self, c):
    dictie = {}
    options = [(self.x-1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y)]
    for x in options:
        dictie[x] = cmd(x,c)
    y = min(dictie.values())
    n = [x for x in dictie if dictie[x] == y]
    coord = sorted(n)[0]
    self.x = coord[0]
    self.y = coord[1]




class Goblin:
    def __init__(self, x, y, id=None):
        self.id = id
        self.x = x
        self.y = y
        self.hp = 200
        self.alive = True
    
    @property
    def nearest(self):
        options = [(self.x-1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y)]
        for x in options:
            people = [a for a in alll if a.x == x[0] and a.y == x[1]]
            if people:
                options.remove(x)
        return options
    
    def move(self):
        in_range = set()
        x = [e.nearest for e in elves if e.alive]
        for p in x:
            for q in p:
                in_range.add(q)
        reachable = reach(self,in_range)
        if reachable:
            nearest = md((self.x,self.y),reachable)
            if nearest != "Attack":
                chosen = choose(nearest)
                walk(self, chosen)
        self.attack()
    
    def attack(self):
        options = [(self.x-1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y)]
        for x in options:
            elf = [e for e in elves if e.x == x[0] and e.y == x[1]]
            if elf:
                elf = elf[0]
                elf.hp -=3
                if elf.hp <= 0:
                    elf.kill()
                return
    def kill(self):
        self.alive = False
        goblins.remove(self)
        alll.remove(self)
                     
class Elf:
    def __init__(self, x, y, id=None):
        self.id = id
        self.x = x
        self.y = y
        self.hp = 200
        self.alive = True   
    
    @property
    def nearest(self):
        options = [(self.x-1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y)]
        for x in options:
            people = [a for a in alll if a.x == x[0] and a.y == x[1]]
            if people:
                options.remove(x)
        return options
    
    def move(self):
        in_range = set()
        x = [g.nearest for g in goblins if g.alive]
        for p in x:
            for q in p:
                in_range.add(q)
        reachable = reach(self,in_range)
        if reachable:
            nearest = md((self.x,self.y),reachable)
            if nearest != "Attack":
                chosen = choose(nearest)
                walk(self, chosen)
        self.attack()
    
    def attack(self):
        options = [(self.x-1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y)]
        for x in options:
            goblin = [g for g in goblins if g.x == x[0] and g.y == x[1]]
            if goblin:
                goblin = goblin[0]
                goblin.hp -=3
                if goblin.hp <= 0:
                    goblin.kill()
                return
    def kill(self):
        self.alive = False
        elves.remove(self)
        alll.remove(self)

elves = []
goblins = []
alll=[]

for y in range(0, len(inputt)):
    for x in range(0, len(inputt[y])):
        if inputt[y][x] == "E":
            e = Elf(x,y)
            elves.append(e)
            alll.append(e)
        elif inputt[y][x] == "G":
            g = Goblin(x,y)
            goblins.append(g)
            alll.append(g)

def ss(x):
    return x.x, x.y

round=0

while len([e for e in elves if e.alive]):
    round+=1
    print(round)
    elves.sort(key=ss)
    goblins.sort(key=ss)
    alll.sort(key=ss)
    for y in alll:
        if y.alive:
            y.move()
    

print("ALL OK")
        
            
        
