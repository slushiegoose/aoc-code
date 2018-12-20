with open("Day 9.txt","r") as f: inputt=f.read().strip()
#with open("example.txt","r") as f: inputt=f.read().strip()


players = int(inputt.split(" ")[0])
points = int(inputt.split("worth ")[1].split(" ")[0])

class Marble:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

    def add_marble(self, nv):
        if nv % 23:
            new = Marble(nv)
            one = self.next
            two = self.next.next
            new.prev = one
            new.next = two
            one.next = new
            two.prev = new
            return new, 0
        else:
            past = self
            for x in range(7):
                past = past.prev
            past.next.prev = past.prev
            past.prev.next = past.next
            return past.next, (nv + past.value)

p_num = 0
x=0
cm = Marble(0)
player_list = [0 for x in range(players)]
while cm.value != points * 100:
    cm, score = cm.add_marble(x)
    player_list[p_num]+=score
    p_num+=1
    p_num%=players
    x+=1
print(max(player_list))





