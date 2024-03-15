import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

cnt = 0

# for i in range(n):
#     flag = False
#     for j in range(n - 1):
#         if arr[j] > arr[j + 1]:
#             flag = True 

#     if flag:
#         cnt += 1

# print(cnt)

idx = n - 2
while idx >= 0 and arr[idx] < arr[idx + 1]:
    idx -= 1

print(idx + 1)