from collections import deque
import sys

si = sys.stdin.readline

n = int(si())
q = deque()

for _ in range(n):
    command = si().strip()
    if command[0:4] == "push":
        q.append(int(command[5:len(command)]))

    elif command == "front":
        print(q[0])

    elif command == "size":
        print(len(q))

    elif command == "empty":
        if q:
            print('0')
        else:
            print('1')

    elif command == "pop":
        print(q.popleft())