import sys
from functools import cmp_to_key

si = sys.stdin.readline

n = int(si())
brackets = []

answer = 0

def compare(b1, b2):
    open1, closed1 = b1
    open2, closed2 = b2

    if open1 * closed2 > open2 * closed1:
        return -1

    if open1 * closed2 > open2 * closed1:
        return 1
    
    return 0

for _ in range(n):
    s = si().strip()
    open_num, closed_num = 0, 0
    for char in s:
        if char == '(':
            open_num += 1
        else:
            closed_num += 1

            answer += open_num
    
    brackets.append((open_num, closed_num))

brackets.sort(key=cmp_to_key(compare))

open_sum = 0
for open_num, closed_num in brackets:
    answer += open_sum * closed_num
    open_sum += open_num 

print(answer)