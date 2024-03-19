import sys
from collections import defaultdict
from sortedcontainers import SortedSet

# 가장 많이 등장한 숫자 부터 출력 동일한 경우 라면 값이 더 큰 숫자부터 출력
# 보통 문제부터는 두가지 이상의 자료구조들을 혼용해야 풀릴거 같다, 아니면 같은 자료구조를 두번 이상 사용하여 활용

si = sys.stdin.readline

n, k = map(int, si().split())

arr = list(map(int, si().split()))

d = defaultdict(int)
ss = SortedSet()

# for elem in a:
#     if elem in d:
#         d[elem] += 1
#     else:
#         d[elem] = 1

for elem in arr:
    d[elem] += 1

for elem in d:
    ss.add((d[elem], elem))

for _ in range(k):
    value, key = ss.pop(-1)
    if d[key] != 0:
        print(key, end=" ")
        d[key] = 0