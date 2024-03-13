import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

min_max_cnt = sys.maxsize

for i in range(102):
    for j in range(102):
        quad_1_cnt = 0
        quad_2_cnt = 0
        quad_3_cnt = 0
        quad_4_cnt = 0
        quad_max_cnt = 0
        flag = True
        for x, y in arr:
            if x == i or y == j:
                flag = False
                break
            
            if x > i and y > j:
                quad_1_cnt += 1
            elif x < i and y > j:
                quad_2_cnt += 1
            elif x < i and y < j:
                quad_3_cnt += 1
            elif x > i and y < j:
                quad_4_cnt += 1

        if flag:
            quad_max_cnt = max(quad_1_cnt, quad_2_cnt, quad_3_cnt, quad_4_cnt)
            min_max_cnt = min(min_max_cnt, quad_max_cnt)

print(min_max_cnt)