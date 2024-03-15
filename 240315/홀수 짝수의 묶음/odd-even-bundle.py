import sys

si = sys.stdin.readline 

# 짝수먼저 짝 / 홀 / 짝 / 홀

n = int(si())
arr = list(map(int, si().split()))

# flag = 0 # flag 가 짝수이면 짝수를, 홀수이면 홀수를 만들어야 함 
# answer = 0
# i = 0
# while i < n:
#     local_sum = 0
#     j = i
#     while j < n:
#         local_sum += arr[j]
#         if local_sum % 2 == 0 and flag % 2 == 0:
#             answer += 1
#             flag += 1
#             i = j
#             break

#         elif local_sum % 2 == 1 and flag % 2 == 1:
#             answer += 1
#             flag += 1
#             i = j
#             break

#         else:
#             j += 1
#     i += 1
            
# print(answer)
        
even = 0
odd = 0
for elem in arr:
    if elem % 2 == 0:
        even += 1
    else:
        odd += 1

group_num = 0
while True:
    if group_num % 2 == 0:
        if even:
            even -= 1
            group_num += 1
        elif odd >= 2:
            odd -= 2
            group_num += 1
        else:
            if even > 0 or odd > 0:
                group_num -= 1
            break
    
    else:
        if odd:
            odd -= 1
            group_num += 1

        else:
            break

print(group_num)