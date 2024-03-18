import sys
from collections import deque

si = sys.stdin.readline

n = int(si())

q = deque()

for _ in range(n):
    command = si().strip()
    if command[0:9] == "push_back":
        q.append(command[10:len(command)])

    elif command[0:10] == "push_front":
        q.appendleft(command[11:len(command)])

    elif command[0:5] == "front":
        print(q[0])

    elif command[0:4] == "back":
        print(q[-1])

    elif command[0:9] == "pop_front":
        print(q.popleft())

    elif command[0:8] == "pop_back":
        print(q.pop())

    elif command[0:4] == "size":
        print(len(q))

    elif command[0:5] == "empty":
        if q:
            print('0')
        else:
            print('1')