import sys

si = sys.stdin.readline


def preprocess():
    dp[2] = 1
    dp[3] = 1

    for i in range(5, 1001):
        dp[i] = dp[i - 2] + dp[i - 3]
        dp[i] %= 10007

n = int(si())

dp = [0] * 1001

preprocess()
print(dp[n])