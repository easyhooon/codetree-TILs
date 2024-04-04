import sys

# 모든 연속된 구간의 합 중에서 -> k개 라는 제한이 없음
# n 은 1000이하 2중 포문 가능

si = sys.stdin.readline

n, k = map(int, si().split())
arr = list(map(int, si().split()))

ps = [0 for _ in range(n)]

for i in range(n):
    ps[i] = arr[i]
    if i > 0:
        ps[i] += ps[i - 1]

cnt = 0
# s 와 e 가 같을  때 를 추가해야함 
for s in range(0, n):
    for e in range(s, n):
        if s > 0:
            if ps[e] - ps[s - 1] == k:
                cnt += 1
        else:
            if ps[e] == k:
                cnt += 1
print(cnt)