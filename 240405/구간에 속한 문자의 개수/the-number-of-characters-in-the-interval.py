import sys

si = sys.stdin.readline

n, m, k = map(int, si().split())

a = [
    list(map(str, si())) for _ in range(n)
]

ps = [
    [
        [0 for _ in range(3)]
        for _ in range(m)
    ]
    for _ in range(n)
]

# ps 계산 하기 (!차원과 논리는 같다)
for i in range(n):
    for j in range(m):
        if a[i][j] == 'a':
            ps[i][j][0] = 1
        elif a[i][j] == 'b':
            ps[i][j][1] = 1
        elif a[i][j] == 'c':
            ps[i][j][2] = 1

        if i > 0:
            for g in range(3):
                ps[i][j][g] += ps[i - 1][j][g]
        if j > 0:
            for g in range(3):
                ps[i][j][g] += ps[i][j - 1][g]
        if i > 0 and j > 0:
            for g in range(3):
                ps[i][j][g] -= ps[i - 1][j - 1][g]

for _ in range(k):
    sx, sy, ex, ey = map(int, si().split())

    # 시간 복잡도 O(n^2)

    # (r1, c1) ~ (r2, c2)
    a_cnt, b_cnt, c_cnt = ps[ex - 1][ey - 1][0], ps[ex - 1][ey - 1][1], ps[ex - 1][ey - 1][2]
    if sx > 1:
        a_cnt -= ps[sx - 2][ey - 1][0]
        b_cnt -= ps[sx - 2][ey - 1][1]
        c_cnt -= ps[sx - 2][ey - 1][2]
    if sy > 1:
        a_cnt -= ps[ex - 1][sy - 2][0]
        b_cnt -= ps[ex - 1][sy - 2][1]
        c_cnt -= ps[ex - 1][sy - 2][2]
    if sx > 1 and sy > 1:
        a_cnt += ps[sx - 2][sy - 2][0]
        b_cnt += ps[sx - 2][sy - 2][1]
        c_cnt += ps[sx - 2][sy - 2][2]

    print(a_cnt, b_cnt, c_cnt)