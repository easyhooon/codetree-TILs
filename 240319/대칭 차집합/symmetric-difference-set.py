import sys

si = sys.stdin.readline


# 대칭 차집합 : 합집합 - 교집합
n, m = map(int, si().split())
a = list(map(int, si().split()))
b = list(map(int, si().split()))

a_set = set(a)
b_set = set(b)

# a 에만 속한 원소
x = 0
for elem in a:
    if elem not in b_set:
        x += 1

# b 에만 속한 원소
y = 0
for elem in b:
    if elem not in a_set:
        y += 1

print(x + y)