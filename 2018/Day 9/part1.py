with open("Day 9.txt","r") as f: inputt=f.read().strip()
#with open("example.txt","r") as f: inputt=f.read().strip()


players = int(inputt.split(" ")[0])
points = int(inputt.split("worth ")[1].split(" ")[0])


listie = []

marble_list = [0]

for x in range(players):
    listie.append(0)

cm = 0
x = 0
eye = 0

player_num = 0

while True:
    #print(marble_list)
    if (cm+1) % 23:
        eye+=1
        eye%= len(marble_list)
        eye+=1
        if not eye:
            marble_list.append(cm+1)
            eye = len(marble_list)-1
        else:
            marble_list.insert(eye,cm+1)
        player_num +=1
        player_num %= players
        cm +=1
        x = int(cm)
    else:
        listie[player_num] += cm+1
        #print(cm+1)
        eye-=7
        eye %= len(marble_list)
        append = marble_list.pop(eye)
        listie[player_num] += append
        print(player_num,"given",append+cm+1)
        #print(append + cm + 1)
        cm +=1
        x = marble_list[eye]
        player_num +=1
        player_num %= players
    if cm>points+1:break

#print(marble_list)
print(listie)
print(max(listie))




