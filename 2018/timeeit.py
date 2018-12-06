import sys
import os
from subprocess import run, PIPE

class Day:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        x = '/home/suhailm0608/My deep, dark coding hole/AoC/2018/Day {}'.format(newPath)
        self.newPath = os.path.expanduser(x)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


listie = []

for x in range(1,7):
    with Day(x):
        listie.append(os.popen("time python3 part1.py").read())
        listie.append(os.popen("time python3 part2.py").read())

print(listie)
        
        