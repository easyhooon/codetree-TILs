import sys

# 문자열을 정렬해서 hashMap 에 넣자
# ''.join 의 용도 
si = sys.stdin.readline

n = int(si())

d = dict()

for i in range(n):
    cmd = ''.join(sorted(si().strip()))
    if cmd in d:
        d[cmd] += 1
    else:
        d[cmd] = 1

answer = -sys.maxsize
for key, value in d.items():
    answer = max(answer, value)

print(answer)