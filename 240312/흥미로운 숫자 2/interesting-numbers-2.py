import sys
from collections import Counter

si = sys.stdin.readline

x, y = map(int, si().split())

def is_exciting_num(num):
    counter = Counter(list(str(num)))
    if len(counter.keys()) == 2:
        if counter[list(counter.keys())[0]] == 1 or counter[list(counter.keys())[1]] == 1:
            return True

        else: 
            return False
    else:
        return False

cnt = 0
for i in range(x, y + 1):
    if is_exciting_num(i):
        cnt += 1

print(cnt)