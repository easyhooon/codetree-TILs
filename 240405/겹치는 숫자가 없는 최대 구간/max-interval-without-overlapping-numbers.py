import sys

si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))

counting = [0 for _ in range(100001)]

R = -1
ans = 0
for L in range(n):
    # R이 이동할 수 있을 때
    while R + 1 < n and counting[a[R + 1]] == 0:
        # R 확장
        R += 1
        # 이동 갱신
        counting[a[R]] = 1
    ans = max(ans, R - L + 1)
    counting[a[L]] = 0

print(ans)