from sortedcontainers import SortedSet
import sys

si = sys.stdin.readline 

# 더 큰 점수를 가진 빨간돌을 어디에 넣어야 할까 

c, n = map(int, si().split())
red_stones = [
    int(si())
    for _ in range(c)
]
black_stones = []
for _ in range(n):
    a, b = map(int, si().split())
    black_stones.append((b, a))

red_s = SortedSet(red_stones)
black_stones.sort()

answer = 0
for b, a in black_stones:
    idx = red_s.bisect_left(a)
    if idx != len(red_s):
        ti = red_s[idx]
        if ti <= b:
            answer += 1
            red_s.remove(ti)

print(answer)