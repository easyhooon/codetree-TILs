import sys
from collections import defaultdict

si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
a_set = set(a)  

m = int(si())
b = list(map(int, si().split()))
b_set = set(b)  

d = defaultdict(int) # int라고 지정해야 초기값이 0으로 지정됨, default 초기값은 0임 

for elem in a_set:
    if elem in b_set:
        d[elem] = 1

for i in range(m):
    print(d[b[i]], end=" ")