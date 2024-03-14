import sys

si = sys.stdin.readline

arr = [
    list(si().strip())
    for _ in range(3)
]

# print(arr)

cnt = 0
for i in range(3):
    temp_arr = []
    for j in range(3):
        temp_arr.append(arr[i][j])
    temp_arr = set(temp_arr)
    if len(temp_arr) == 2:
        cnt += 1

for i in range(3):
    temp_arr = []
    for j in range(3):
        temp_arr.append(arr[j][i])
    temp_arr = set(temp_arr)
    if len(temp_arr) == 2:
        cnt += 1

temp_arr = []
temp_arr.append(arr[0][0])
temp_arr.append(arr[1][1])
temp_arr.append(arr[2][2])
temp_arr = set(temp_arr)
if len(temp_arr) == 2:
    cnt += 1

temp_arr = []
temp_arr.append(arr[0][2])
temp_arr.append(arr[1][1])
temp_arr.append(arr[2][0])
temp_arr = set(temp_arr)
if len(temp_arr) == 2:
    cnt += 1

print(cnt)