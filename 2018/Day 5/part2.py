path = __file__.split("part")[0]
def main():
    with open(path + "Day 5.txt","r") as f: hh=f.read().strip()
    # inputt = "dabAcCaCBAcCcaDA"

    p = 0


    def check(x,y):
        return x.lower() == y.lower() and x!=y

    # print(len(hh))

    def solve(inputt):
        r1 = inputt
        l1 = len(r1)
        l2 = l1+1
        while l1 != l2:
            l2 = l1
            for c in 'qwertyuiopasdfghjklzxcvbnm':
                r1 = r1.replace(c+c.upper(), '').replace(c.upper()+c, '')
            l1 = len(r1)
        return l1

    dictie = {}

    for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        templist = []
        p=0
        dictie[x] = solve(hh.replace(x.lower(),"").replace(x.upper(),""))


    # print(dictie)
    ma = min(dictie.values())
    # print(ma)


