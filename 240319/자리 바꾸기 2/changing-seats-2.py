import sys

si = sys.stdin.readline

n, k = map(int, si().split())

change = [
    list(map(int, si().split()))
    for _ in range(k)
]

s = [set() for _ in range(n + 1)]
answer = [0 for _ in range(n + 1)]

arr = [i for i in range(n + 1)]

for i in range(1, n + 1):
    s[i].add(i)
    answer[i] = 1

for _ in range(3):
    for (a, b) in change:
        arr[a], arr[b] = arr[b], arr[a]

        if a not in s[arr[a]]:
            s[arr[a]].add(a)
            answer[arr[a]] += 1

        if b not in s[arr[b]]:
            s[arr[b]].add(b)
            answer[arr[b]] += 1

for i in range(1, n + 1):
    print(answer[i])