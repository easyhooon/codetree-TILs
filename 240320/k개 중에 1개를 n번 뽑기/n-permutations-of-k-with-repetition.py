# 중복을 허용
import sys

si = sys.stdin.readline

k, n = map(int, si().split())

answer = []

def choose(curr_num):
    if curr_num == n + 1:
        for elem in answer:
            print(elem, end=" ")
        print()

    else:
        for i in range(1, k + 1):
            answer.append(i)
            choose(curr_num + 1)
            answer.pop()

choose(1)