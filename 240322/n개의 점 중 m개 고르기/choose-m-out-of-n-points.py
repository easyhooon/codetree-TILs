import sys

si = sys.stdin.readline 

n, m = map(int, si().split())

arr = []
combination = []
 
answer = sys.maxsize

for _ in range(n):
    x, y = map(int, si().split())
    arr.append((x, y))

def find_max_dist(comb):
    global m
    max_dist = -sys.maxsize

    for i in range(m - 1):
        for j in range(i + 1, m):
            dist = (comb[i][0] - comb[j][0]) ** 2 + (comb[i][1] - comb[j][1]) ** 2
            max_dist = max(max_dist, dist)
    return max_dist

def find_combination(curr_num, cnt):
    global n, m, answer
    # cutting
    if cnt > m:
        return

    if curr_num == n:
        if cnt == m:
            max_dist = find_max_dist(combination)
            answer = min(answer, max_dist)
        return

    combination.append(arr[curr_num])
    find_combination(curr_num + 1, cnt + 1)
    combination.pop()

    find_combination(curr_num + 1, cnt)

find_combination(0, 0)

print(answer)