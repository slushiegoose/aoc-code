with open("josh.txt","r") as f: hh=f.read().strip()
# inputt = "dabAcCaCBAcCcaDA"

p = 0

hh = list(hh)

def check(x,y):
    return x.lower() == y.lower() and x!=y

# print(len(hh))

def solve(inputt):
    p = 0
    solved = True
    while True:
        try:
            if check(inputt[p],inputt[p+1]):
                del inputt[p]
                del inputt[p]
                solved = False
                continue
            else: p+=1
        except Exception as e:
            # print(e)
            # print(solved)
            if solved:
                break
            p=0
            solved = True
            continue
    return len(inputt)

print(solve(hh))