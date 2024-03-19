import sys
from collections import deque

si = sys.stdin.readline

n, g = map(int, si().split())

invited = [False] * n
# 각 그룹마다 초대장을 받지 못한 사람들을 관리
groups = [set() for _ in range(g)]
# 각 사람이 어떤 그룹에 속하는지 관리
people_groups = [[] for _ in range(n)]

q = deque()
answer = 0

for i in range(g):
    nums = list(map(int, si().split()))[1:]
    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i)

q.append(0)
invited[0] = True

while(q):
    x = q.popleft()
    answer += 1

    for g_num in people_groups[x]:
        groups[g_num].remove(x)
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)

print(answer)