import sys

si = sys.stdin.readline

n, k = map(int, si().split())
arr = list(map(int, si().split()))

count = dict()

for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

ans = 0
# 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
for i in range(n):
    # 이미 순회한 적이 있는 숫자는 빼 버림으로서
    # 같은 조합이 여러번 세어지는 걸 방지합니다.
    count[arr[i]] -= 1

    # 0 <= j <= i - 1
    for j in range(i):
        # 전처리를 해주었기 때문에 이미 순회한 적 있는 값은 hashmap에 없습니다.
        # 이와 같은 방식으로 같은 조합이 중복되어 세어지는 걸 방지할 수 있습니다.
        diff = k - arr[i] - arr[j]

        if diff in count:
            ans += count[diff]

print(ans)