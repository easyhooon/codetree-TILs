import sys

si = sys.stdin.readline
MOD = 10007


def preprocess():
    dp[1] = 1
    dp[2] = 3

    for i in range(4, 1001):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD


n = int(si())

dp = [0] * 1001

preprocess()
print(dp[n])