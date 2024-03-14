import sys

si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(int, si().split()))

# 최소한의 와이파이 개수 -> 와이파이 영역이 겹치지 않게 설치(2 * m + 1)
# 처음 와이파이를 놓아야 하는 위치는 가장 왼쪽 집에 사는 사람을 커버하는 가장 오른쪽 위치에 놓는 것이 좋다
cnt, i = 0, 0
while i < n:
    if arr[i] == 1:
        cnt += 1
        # print(i)
        i += 2 * m + 1
    else:
        i += 1
print(cnt)