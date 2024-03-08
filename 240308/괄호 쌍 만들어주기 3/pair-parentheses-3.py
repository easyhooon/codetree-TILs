import sys

si = sys.stdin.readline

n = list(si())

len_n = len(n)

cnt = 0
for i in range(len_n - 1):
    for j in range(i + 1, len_n):

        if n[i] + n[j] == '()':
            cnt += 1

print(cnt)