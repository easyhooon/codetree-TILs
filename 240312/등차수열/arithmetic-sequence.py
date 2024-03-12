import sys

si = sys.stdin.readline

n = int(si())

arr = list(map(int, si().split()))
arr.sort()
start = arr[0]
end = arr[len(arr) - 1]

max_cnt = -sys.maxsize
for i in range(start ,end + 1):
    cnt = 0
    for j in range(n - 1):
        for k in range(1, n):
            if j + k < n:
                if abs(i - arr[j]) == abs(i - arr[j + k]):
                    cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)