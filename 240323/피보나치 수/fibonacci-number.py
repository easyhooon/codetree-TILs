import sys

si = sys.stdin.readline

n = int(si())

def fibo(n):
    if memo[n] != -1:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
    else:
        memo[n] =  fibo(n - 1) + fibo(n - 2)

    return memo[n]

memo = [-1] * 46

print(fibo(n))