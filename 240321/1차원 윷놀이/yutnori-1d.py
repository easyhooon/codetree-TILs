import sys

si = sys.stdin.readline

# 처음에는 k개의 말이 1번지점에 놓여있다 (0번이 아님 1번임) 

# n: 턴의 수
# m: 판의 칸 수
# k: 말의 수 
n, m, k = map(int, si().split())
# n 개의 수가 주어짐, 각 턴마다 나아갈 수 있는 거리 
arr = list(map(int, si().split()))

# 얻을 수 있는 점수를 최대로 

max_point = -sys.maxsize
candidate = []

def find_max_point():
    global k
    # 각각의 말에 대해서 현재 위치를 관리하는 배열이 필요
    point = 0
    # state = [0 for _ in range(k)] 
    state = [1] * k 
    for i in range(n):
        jump_cnt, num = candidate[i]
        state[num] += jump_cnt

    for i in range(k):
        if state[i] >= m:
            point += 1

    return point

def find_max(index):
    global max_point
    if index == n:
        max_point = max(max_point, find_max_point())
        return

    for i in range(k):
        candidate.append((arr[index], i))
        find_max(index + 1)
        candidate.pop()

find_max(0)
print(max_point)