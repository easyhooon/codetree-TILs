import sys
from collections import defaultdict


# 서로 다른 위치에 있는 두 개의 수를 뽑아 더했을 때 k가 되는 가짓 수
# 중복을 허용, 다른 위치에 있으면 다른 수

si = sys.stdin.readline

n, k = map(int, si().split())

a = list(map(int, si().split()))

d = defaultdict()

for elem in a:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

cnt = 0

for key, value in d.items():
    if k - key in d:
        if key == k - key:
            cnt += d[key] * (d[key] - 1) # nP2
        else:
            cnt += d[key] * d[k - key]

print(cnt // 2)