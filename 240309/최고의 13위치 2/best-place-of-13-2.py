import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

max_sum = -sys.maxsize

# 서로 겹치지 않게 두곳의 위치를 고르고 합이 최대인 경우의 수 찾기
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):  
                if i == k and (j == l or j + 1 == l or j + 2 == l): 
                    continue
                sum_val = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_sum = max(max_sum, sum_val)

print(max_sum)