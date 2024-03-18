import sys

si = sys.stdin.readline

n = int(si())
arr = []
for _ in range(n):
    command = si().strip()

    if command[0 : 4] == "push":
        arr.append(int(command[5 : len(command)]))
    
    elif command == "size":
        print(len(arr))

    elif command == "empty":
        if arr:
            print('0')
        else:
            print('1')

    elif command[0 : 3] == "pop":
        print(arr[len(arr) - 1])
        arr.pop()

    elif command == "top":
        print(arr[len(arr) - 1])