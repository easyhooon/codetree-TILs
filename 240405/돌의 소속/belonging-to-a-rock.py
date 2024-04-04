import sys

# 각 돌은 그룹 1, 2, 3 중 하나에 무조건 속합니다.
# 각 돌이 어떤 그룹에 속하는지 주어졌을 때, Q개의 돌 번호 범위마다 각 그룹의 돌이 몇개씩 있는지 구하는 프로그램 작성
# 이게 왜 누적합 -> 몇번까지 해당 그룹에 몇명이 속하는지 저장해두어야함

si = sys.stdin.readline

n, q = map(int, si().split())
# i번 그룹이 j번까지 몇명 속해있는지
arr = [[0 for _ in range(3)] for _ in range(n)]
ps = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    group = int(si())
    arr[i][group-1] = 1

# 위에서 부터 차곡차곡 내려와야함;
for i in range(n):
    for j in range(3):
        ps[i][j] = arr[i][j]
        if i > 0:
            ps[i][j] += ps[i-1][j]

# index를 직접 명시해서 -1 씩..
for i in range(q):
    s, e = map(int, si().split())
    if s > 1:
        a, b, c = ps[e-1][0] - ps[s-2][0], ps[e-1][1] -ps[s-2][1], ps[e-1][2] - ps[s-2][2]
    else:
        a, b, c = ps[e-1][0], ps[e-1][1], ps[e-1][2]
    print(a, b, c)