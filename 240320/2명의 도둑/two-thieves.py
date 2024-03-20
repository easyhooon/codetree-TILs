import sys

si = sys.stdin.readline 

n, m, c = map(int, si().split())
weight = [
    list(map(int, si().split()))
    for _ in range(n)
]
arr = []
max_val = 0

def find_max_sum(curr_idx, curr_weight, curr_val):
    global max_val

    if curr_idx == m:
        if curr_weight <= c:
            max_val = max(max_val, curr_val)
        return

    find_max_sum(curr_idx + 1, curr_weight, curr_val)

    find_max_sum(curr_idx + 1, curr_weight + arr[curr_idx], curr_val + arr[curr_idx] * arr[curr_idx])

def find_max(sx, sy):
    global arr, max_val

    arr = weight[sx][sy: sy + m]

    max_val = 0
    find_max_sum(0, 0, 0)
    return max_val 

def intersect(a, b, c, d):
    return not (b < c or d < a)

def possible(sx1, sy1, sx2, sy2):
    if sy1 + m - 1 >= m or sy2 + m - 1 >= n:
        return False 

    if sx1 != sx2:
        return True 

    if intersect(sy1, sy1 + m -1, sy2, sy2 + m -1):
        return False

    return True

answer = max([
    find_max(sx1, sy1) + find_max(sx2, sy2)
    for sx1 in range(n)
    for sy1 in range(n)
    for sx2 in range(n)
    for sy2 in range(n)
    if possible(sx1, sy1, sx2, sy2)
])

print(answer)