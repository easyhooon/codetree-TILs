import sys

si = sys.stdin.readline

n = int(si())

d = dict()

for _ in range(n):
    cmd = si().strip()
    if cmd not in d:
        d[cmd] = 1
    else:
        d[cmd] += 1

answer = -sys.maxsize
for key, value in d.items():
    answer = max(answer, value)

print(answer)