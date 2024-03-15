import sys

si = sys.stdin.readline 

arr = list(map(int, si().split()))

arr.sort()
a = arr[0]
sum_val = arr[len(arr) - 1]
b = arr[1]
c = sum_val - a - b

print(a, b, c)