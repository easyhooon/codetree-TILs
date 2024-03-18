import sys

si = sys.stdin.readline

command = si().strip()
stack = []

if command[0] == ')':
    print('No')
    sys.exit(0)

for i in range(len(command)):
    if command[i] == '(':
        stack.append(command[i])

    else:
        if stack:
            stack.pop()

if stack:
    print('No')

else:
    print('Yes')