import sys

si = sys.stdin.readline

N = int(si())
arr = [] * N
for _ in range(N):
    temp = int(si())
    arr.append(temp)

# # 1번 시작
# 0 1 2 3 4
# 7 x 1 + 8 x 2 + 6 x 3 + 4 x 4 = 
# 7 + 16 + 18 + 16 = 57

# # 2번 시작
# 4 0 1 2 3
# 8 x 1 + 6 x 2 + 4 x 3 + 4 x 4 = 
# 8 + 12 + 12 + 16 = 48

# # 3번 시작
# 3 4 0 1 2
# ...

# # 4번 시작
# 2 3 4 0 1
# ...

# # 5번 시작 
# 1 2 3 4 0

# ... 완탐 후 가장 적은 것 찾기

new_arr = []

cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i <= j:
            cnt += arr[j] * (j - i)
        else:
            cnt += arr[j] * (N - abs(j - i))
    new_arr.append(cnt)

print(min(new_arr))