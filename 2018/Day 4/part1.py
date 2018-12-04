with open("Day 4.txt","r") as f: inputt=f.readlines()

# inputt = """[1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up""".split("\n")



guards_len = {}
guards_min = {}



def key(x):
    month = int(x.split("-")[1])
    day = int(x.split("-")[2].split(" ")[0])
    hour = int(x.split(" ")[1].split(":")[0])
    minute = int(x.split(":")[1].split("]")[0])
    return month, day, hour, minute



inputt.sort(key=key)

print(inputt)
guard = None
sleep = True
minute = None

for x in inputt:
    if "#" in x:
        guard = x.split("#")[1].split(" ")[0]
        print(guard + "guard")
    elif "asleep" in x:
        minute = int(x.split(":")[1].split("]")[0])
        print("min",minute)
    elif "wakes" in x:
        new_min = int(x.split(":")[1].split("]")[0])
        print("new_min",new_min)
        length = new_min - minute
        if guard in guards_len:
            guards_len[guard]+=length
        else:
            guards_len[guard]=length
        if guard not in guards_min:
            guards_min[guard] = {}
        for x in range(minute, new_min):
            if x in guards_min[guard]:
                guards_min[guard][x]+=1
            else:
                guards_min[guard][x]=1


maximum = max(guards_len.values())
guard = [x for x in guards_len if guards_len[x]==maximum][0]
print(guards_len)
# print(guard)


max_min = max(guards_min[guard].values())
min = [x for x in guards_min[guard] if guards_min[guard][x]==max_min][0]
print(guards_min)
print(max_min)
print(int(guard)*min)





