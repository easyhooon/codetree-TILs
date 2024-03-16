import sys

si = sys.stdin.readline

# n 이 50,000 이기 때문에 n^2 일 경우 25억 -> 시간초과 
# n 또는 nlogn 으로 문제를 풀어야함 

n = int(si())
a_arr = []
b_arr = []
# arr = [0 for _ in range(2 * n + 1)]
arr = [0] * (2 * n + 1)

# 1: B가 가진 카드, 0: A가 가진 카드, -1: A가 이미 낸 카드 
for _ in range(n):
    num = int(si())
    arr[num] = 1

score = 0
i = 1
while i < 2 * n + 1:
    if arr[i] == 1:
        for j in range(i + 1, 2 * n + 1):
            if arr[j] == 0:
                score += 1
                arr[j] = -1 # 이미 사용한 카드 
                break
    i += 1

print(score)