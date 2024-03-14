import sys

si = sys.stdin.readline

arr = [
    list(si().strip())
    for _ in range(3)
]

# print(arr)
answer = []

for i in range(3):
    temp_arr = []
    for j in range(3):
        temp_arr.append(arr[i][j])
    temp_arr = set(temp_arr)
    if len(temp_arr) == 2:
        temp_arr = list(temp_arr)
        temp_arr.sort()
        answer.append((temp_arr[0], temp_arr[1]))

for i in range(3):
    temp_arr = []
    for j in range(3):
        temp_arr.append(arr[j][i])
    temp_arr = set(temp_arr)
    if len(temp_arr) == 2:
        temp_arr = list(temp_arr)
        temp_arr.sort()
        answer.append((temp_arr[0], temp_arr[1]))

temp_arr = []
temp_arr.append(arr[0][0])
temp_arr.append(arr[1][1])
temp_arr.append(arr[2][2])
temp_arr = set(temp_arr)
if len(temp_arr) == 2:
    temp_arr = list(temp_arr)
    temp_arr.sort()
    answer.append((temp_arr[0], temp_arr[1]))

temp_arr = []
temp_arr.append(arr[0][2])
temp_arr.append(arr[1][1])
temp_arr.append(arr[2][0])
temp_arr = set(temp_arr)
if len(temp_arr) == 2:
    temp_arr = list(temp_arr)
    temp_arr.sort()
    answer.append((temp_arr[0], temp_arr[1]))

answer = set(answer)
print(len(answer))