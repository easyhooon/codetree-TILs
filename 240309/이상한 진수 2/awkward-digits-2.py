import sys

si = sys.stdin.readline

N = list(si())

new_arr = []

for i in range(len(N)):
    N[i] = int(N[i])

for i in range(len(N)):
    if N[i] == 1:
        N[i] = 0
        num = 0
        for j in range(len(N)):
            num = num * 2 + N[j]

        new_arr.append(num)
        N[i] = 1
    else:
        N[i] = 1
        num = 0
        for j in range(len(N)):
            num = num * 2 + N[j]

        new_arr.append(num)
        N[i] = 0

print(max(new_arr))