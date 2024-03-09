import sys

si = sys.stdin.readline

arr = list(si())
len_arr = len(arr)

cnt = 0
# 연속한 여는 괄호, 연속한 닫는 괄호
for i in range(len_arr - 3):
    for j in range(i + 2, len_arr - 1):
        if arr[i] == '(' and arr[i + 1] == '(' and arr[j] == ')' and arr[j + 1] == ')':
            cnt += 1

print(cnt)