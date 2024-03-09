import sys

si = sys.stdin.readline 

n = int(si())
arr = []

for _ in range(n):
    temp = int(si())
    arr.append(temp)

max_sum = -sys.maxsize

# 캐리가 발생하지 않으면서 최대 합 
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            # 각 자리의 수의 합이 10이 넘지 않는지 검사 
            max_num = max(arr[i], arr[j], arr[k])
            max_len = len(str(max_num))
            flag = True
            for l in range(1, max_len + 1):
                sum_val = 0
                # 1의 자리부터 비교해야 함
                if l <= len(str(arr[i])):
                    sum_val += int(str(arr[i])[len(str(arr[i])) - l])
                if l <= len(str(arr[j])):
                    sum_val += int(str(arr[j])[len(str(arr[j])) - l])
                if l <= len(str(arr[k])):
                    sum_val += int(str(arr[k])[len(str(arr[k])) - l])
                if sum_val >= 10:
                    flag = False
                    break
            if (flag):
                max_sum = max(max_sum, arr[i] + arr[j] + arr[k])
print(max_sum)