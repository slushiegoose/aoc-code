with open("Day 8.txt","r") as f: inputt = f.read().strip()
# with open("example.txt","r") as f: inputt = f.read().strip()


data = list(map(int, inputt.split(" ")))
# print(data)
# exit()

parents = {}

metadatas = []

id_num = 1

parents[0] = [data[0],data[1]]


p = 2

exp_child = True
exp_md = False
md_left = 0


while p < len(data):
    # print(id_num)
    # print(parents)
    if exp_child:
        # print("EXP_CHILD")
        ch = data[p]
        md = data[p+1]
        parents[id_num] = [ch,md]
        # print(parents)
        p+=2
        if not ch:
            # print("INVERSE MD")
            exp_child = False
            exp_md = True
        else:
            id_num+=1
    elif exp_md:
        num = data[p]
        p+=1
        # print("EXP_MD",num)
        # print(parents)
        metadatas.append(num)
        parents[id_num][1]-=1
        if not parents[id_num][1]:
            del parents[id_num]
            id_num-=1
            if id_num < 0: print("ID_NUM");break
            parents[id_num][0] -=1
            if not parents[id_num][0]:
                exp_child = False
                exp_md = True
                md_left = parents[id_num][1]
            else:
                exp_child = True
                exp_md = False
                id_num+=1

print(metadatas)
print(sum(metadatas))