import sys

si = sys.stdin.readline

k, n = map(int,si().split())

arr = [
    list(map(int, si().split()))
    for _ in range(k)     
]

# 두개의 숫자를 골라 서로간의 관계가 항상 같은 경우(i > j) 인 순서쌍 찾기
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        is_always = True
        for l in range(k):
            if arr[l].index(i) < arr[l].index(j):
                continue
            else:
                is_always = False
                break

        if is_always:
            cnt += 1

print(cnt)