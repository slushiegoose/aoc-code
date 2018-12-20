with open("Day 19.txt","r") as f: inputt = f.readlines()
# with open("example.txt","r") as f: inputt=f.readlines()

ip = inputt.pop(0).strip("#ip ")

ip = int(ip)

registers = [0] * 6
registers[0] = ip

def addr(a, b, c):
    registers[c] = registers[a] + registers[b]

def addi(a, b, c):
    registers[c] = registers[a] + b

def mulr(a, b, c):
    registers[c] = registers[a] * registers[b]

def muli(a, b, c):
    registers[c] = registers[a] * b

def banr(a, b, c):
    registers[c] = registers[a] & registers[b]

def bani(a, b, c):
    registers[c] = registers[a] & b

def borr(a, b, c):
    registers[c] = registers[a] | registers[b]

def bori(a, b, c):
    registers[c] = registers[a] | b

def setr(a, b, c):
    registers[c] = registers[a]

def seti(a, b, c):
    registers[c] = a

def gtir(a, b, c):
    registers[c] = a>registers[b]

def gtri(a, b, c):
    registers[c] = registers[a]>b

def gtrr(a, b, c):
    registers[c] = registers[a]>registers[b] 

def eqir(a, b, c):
    registers[c] = a==registers[b] 

def eqri(a, b, c):
    registers[c] = registers[a]==b

def eqrr(a, b, c):
    registers[c] = registers[a] == registers[b] 
opcode = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]
# print(len(inputt))
while ip < len(inputt):
    registers[0] = ip
    command = inputt[ip]
    x, a, b, c = command.split(" ")
    x = [y for y in opcode if y.__name__ == x][0]
    a,b,c = tuple(map(int, (a,b,c)))
    x(a,b,c)
    ip = registers[0]+1
    # print(ip < len(inputt))
    # print(ip)
    
print(registers)