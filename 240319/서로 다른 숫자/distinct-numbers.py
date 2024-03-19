import sys

si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
a_set = set(a)

print(len(a_set))