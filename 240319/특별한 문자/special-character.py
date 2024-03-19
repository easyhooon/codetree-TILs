import sys

# 만약 그러한 문자가 여러 개라면, 문자열 내에서 가장 먼저 등장한 문자를 출력합니다.

si = sys.stdin.readline

cmd = list(si().strip())

d = dict()

for elem in cmd:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

cnt = 0
ans = []

for key, value in d.items():
    if value == 1:
        cnt += 1
        ans.append(key)

if ans:
    print(ans[0])
else:
    print("None")