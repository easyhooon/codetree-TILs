import sys

si = sys.stdin.readline

# C <= A + B
arr = list(map(int, si().split()))
arr.sort()
a = arr[0]
sum_val = arr[len(arr) - 1]
b = arr[1]
c = arr[2]
d = sum_val - a - b - c 

print(a, b, c, d)