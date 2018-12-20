with open("Day 16.txt") as f: inputt = f.readlines()
# print(inputt);exit()

def addr(_, a, b, c, *, before, after):
    x = before[::]
    x[c] = before[a] + before[b]
    return x == after

def addi(_, a, b, c, *, before, after):
    x = before[::]
    x[c] = before[a] + b
    return x == after

def mulr(_, a, b, c, *, before, after):
    x = before[::]
    x[c] = before[a] * before[b]
    return x == after

def muli(_, a, b, c, *, before, after):
    x = before[::]
    x[c] = before[a] * b
    return x == after

def banr(_, a, b, c, *, before, after):
    x = before[::]
    x[c] = before[a] & before[b]
    return x == after

def bani(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a] & b
    return x==after

def borr(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a] | before[b]
    return x==after

def bori(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a] | b
    return x==after

def setr(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a]
    return x == after

def seti(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = a
    return x == after

def gtir(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = a>before[b]
    return x == after

def gtri(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a]>b
    return x == after

def gtrr(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a]>before[b] 
    return x == after

def eqir(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = a==before[b] 
    return x == after

def eqri(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a]==b
    return x == after

def eqrr(_, a,b,c,*, before, after):
    x = before[::]
    x[c] = before[a] == before[b] 
    return x == after

opcode = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]

def po(*args, **kwargs):
    r = set()
    for x in opcode:
        result = x(*args,**kwargs)
        if result:
            r.add(x)
    return r

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
    y = po(*args,**kwargs)
    if len(y) >=3:
        count+=1
print(count)