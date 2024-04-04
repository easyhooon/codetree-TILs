import sys

si = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = n + 1
R = -1
cnt = 0 # 현재 구간의 합

for L in range(n):
    # R 포인터가 이동 할 수 있고, 이동해야 할 때
    # 왜 이러면 빠른데?
    # while 문 내에서 R은 최대 n 번만 움직임 (1번 움직이고 끝날 수도 있고, 아예 안 움직일 수 도있음)
    # # 2중 반복문 이지만 전체 프로그램에서 시간복잡도 O(n)에 수행됨
    while R + 1 < n and cnt < s:
        # R 포인터를 한 칸 오른쪽 으로 이동
        # 그 구간에 대한 정보를 기록하는 변수들 갱신
        R += 1
        cnt += a[R]

    if cnt >= s:
        # R - L + 1 : 구간의 길이
        ans = min(ans, R - L + 1)

    cnt -= a[L]

if ans == n + 1:
    ans = -1

print(ans)