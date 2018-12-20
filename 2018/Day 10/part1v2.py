import collections
import re

#with open('day10test.txt') as f:
with open('Day 10.txt') as f:
  lines = [l.rstrip('\n') for l in f]
  lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

map = [[' '] * 200 for j in range(400)]
i = 10081
for (x, y, vx, vy) in lines:
    map[y + i * vy][x + i * vx - 250] = '*'

for m in map:
    print ''.join(m)