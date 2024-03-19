# list 는 n^2 hashSet쓰면 상수 시간 

import sys

si = sys.stdin.readline

n = int(si())

s = set()

for i in range(n):
    command = si()

    if command.startswith("find"):
        if int(command.split(" ")[1]) in s:
            print("true")
        else:
            print("false")

    if command.startswith("add"):
        s.add(int(command.split(" ")[1]))

    if command.startswith("remove"):
        s.remove(int(command.split(" ")[1]))