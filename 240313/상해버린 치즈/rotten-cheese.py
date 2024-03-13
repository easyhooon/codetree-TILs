import sys

si = sys.stdin.readline

n, m, d, s = map(int, si().split())

cheese_eat_info = []
for i in range(d):
    p, x, t = map(int, si().split())
    cheese_eat_info.append((p, x ,t))

sick_info = []
for j in range(s):
    p, t = map(int, si().split())
    sick_info.append((p, t))

answer = 0

for i in range(1, m + 1):
    time = [0] * (n + 1)
    for p, x, t in cheese_eat_info:
        if x != i:
            continue

        person = p
        if time[person] == 0:
            time[person] = t
        elif tme[person] > t:
            time[person] = t 

    possible = True

    for p, t in sick_info:
        person = p
        if time[person] == 0:
            possible = False
        if time[person] >= t:
            possible = False 

    cnt = 0
    if possible:
        for j in range(1, n + 1):
            if time[j] != 0:
                cnt += 1
    
    answer = max(answer, cnt)

print(answer)