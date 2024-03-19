import sys
from collections import defaultdict

si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))

a_set = set(a)

m = int(si())
b = list(map(int, si().split()))

for elem in b:
    if elem in a_set:
        print(1)
    else:
        print(0)