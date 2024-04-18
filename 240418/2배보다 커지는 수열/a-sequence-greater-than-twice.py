import sys

si = sys.stdin.readline

MOD = 1_000_000_007

n, m = map(int, si().split())

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for j in range(1, m + 1):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(m, 0, -1):
        for k in range(j // 2, 0, -1):
            dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

result = 0
for j in range(m, 0, -1):
    result = (result + dp[n][j]) % MOD

print(result)