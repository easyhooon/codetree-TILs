import sys

si = sys.stdin.readline

n = int(si())

arr = [
    int(si())
    for _ in range(n)
]

goal = sum(arr) // n 
# 주는 쪽과 받는 쪽이 정해짐 

answer = 0
for i in range(n):
    if arr[i] < goal:
        answer += (goal - arr[i])

print(answer)