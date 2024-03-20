import sys

si = sys.stdin.readline

k, n = map(int, si().split())
answer = []

def choose(curr_num):
    if curr_num == n + 1:
        for e in answer:
            print(e, end=" ")
        print()
    else:
        for i in range(1, k + 1):
            if curr_num >= 3 and answer[-2] == answer[-1] and answer[-1] == i:
                continue
            answer.append(i)
            choose(curr_num + 1)
            answer.pop()


choose(1)