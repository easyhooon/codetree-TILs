import sys

si = sys.stdin.readline

command = si().strip()
stack = []

for i in range(len(command)):
    if command[i] == '(':
        stack.append(command[i])

    else:
        if not stack:
            print("No")
            sus.exit(0)
        stack.pop()

if stack:
    print('No')

else:
    print('Yes')