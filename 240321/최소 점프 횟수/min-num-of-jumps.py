# 최소 점프 횟수를 모르니 모든 n번째 위치에 도달할 수 있는 모든 점프 횟수를 구해서 최소값을 구하자

import sys

si = sys.stdin.readline

n = int(si())

# 각 위치에서의 최대 점프 가능 거리를 배열에 저장
arr = list(map(int, si().split()))

min_cnt = sys.maxsize

# curr_num: 현재 칸의 위치
# cnt: 점프 횟수
def find_combination(curr_num, cnt):
    global min_cnt
    # n번째 위치에 도달했을 경우
    if curr_num == n - 1:
        min_cnt = min(min_cnt, cnt)

    # 아직 n번째 위치에 도달하지 못한 경우
    # 각 칸에서는 1..arr[curr_num] 만큼 점프가 가능 하다
    for i in range(1, arr[curr_num] + 1):
        # n번째 위치를 넘어서 점프하는 경우 제외
        if curr_num + i > n - 1:
            continue

        else:
            find_combination(curr_num + i, cnt + 1)


find_combination(0, 0)

if min_cnt == sys.maxsize:
    print(-1)
else:
    print(min_cnt)