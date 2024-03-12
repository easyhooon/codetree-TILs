import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            visited = [0] * 101
            for l in range(n):
                if l == i or l == j or l == k:
                    continue

                start = arr[l][0]
                end = arr[l][1]
                for x in range(start, end + 1):
                    visited[x] += 1

            flag = True
            for y in range(101):
                if visited[y] > 1:
                    flag = False
                    break

            if flag:
                cnt += 1

print(cnt)