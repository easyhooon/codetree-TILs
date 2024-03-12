import sys

si = sys.stdin.readline

T, a, b = map(int, si().split())

# arr = [0] * 1001

cnt = 0
# for _ in range(T):
#     c, x = map(str, si().split())
#     if c == 'S':
#         arr[int(x)] = 1
#     else:
#         arr[int(x)] = 2

arr = [
    tuple(si().split())
    for _ in range(T)
]

for i in range(a, b + 1):
    dist_s = sys.maxsize
    dist_n = sys.maxsize

    for p, q in arr:
        q = int(q)
        if p == 'S':
            dist_s = min(dist_s, abs(q - i))
        else:
            dist_n = min(dist_n, abs(q - i))

    if dist_s <= dist_n:
        cnt += 1
        
print(cnt)