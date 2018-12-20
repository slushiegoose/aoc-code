with open("Day 16.txt") as f: inputt = f.readlines()
# print(inputt);exit()



def addr(_, a, b, c, *, before):
    x = before[::]
    x[c] = before[a] + before[b]
    return x

def addi(_, a, b, c, *, before):
    x = before[::]
    x[c] = before[a] + b
    return x

def mulr(_, a, b, c, *, before):
    x = before[::]
    x[c] = before[a] * before[b]
    return x

def muli(_, a, b, c, *, before):
    x = before[::]
    x[c] = before[a] * b
    return x

def banr(_, a, b, c, *, before):
    x = before[::]
    x[c] = before[a] & before[b]
    return x

def bani(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a] & b
    return x

def borr(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a] | before[b]
    return x

def bori(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a] | b
    return x

def setr(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a]
    return x

def seti(_, a,b,c,*, before):
    x = before[::]
    x[c] = a
    return x

def gtir(_, a,b,c,*, before):
    x = before[::]
    x[c] = a>before[b]
    return x

def gtri(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a]>b
    return x

def gtrr(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a]>before[b] 
    return x

def eqir(_, a,b,c,*, before):
    x = before[::]
    x[c] = a==before[b] 
    return x

def eqri(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a]==b
    return x

def eqrr(_, a,b,c,*, before):
    x = before[::]
    x[c] = before[a] == before[b] 
    return x

opcode = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]

ids = {}
count=0
def po(*args, before, after):
    r = []
    for x in opcode:
        result = x(*args,before=before)
        if result == after:
            if x not in ids.values():
                r.append(x)

    if len(r) == 1:
        ids[args[0]] = r[0]


count=0
x=0
while inputt[x].strip():
    before, now, after = inputt[x:x+3]
    x+=4
    before = eval(before[8:])
    after = eval(after[8:])
    kwargs = {"before": before, "after": after}
    args = [int(x) for x in now.split(" ")]
    #print(args,kwargs)
    po(*args,**kwargs)
print(count)
print(ids)
program = inputt[x:]
rest = [p.strip() for p in program if p.strip()]
# print(program);exit()

registers = [0,0,0,0]
for x in rest:
    op, a, b, c = map(int, x.split(" "))
    registers = ids[op](op,a,b,c,before=registers)

print(registers)


