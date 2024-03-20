import sys

si = sys.stdin.readline

n = int(si())
answer = 0
seq = []

def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 설정
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 아름다운 수가 아님
        if i + seq[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인합니다.
        # 하나라도 다른 숫자가 있다면
        # 아름다운 수가 아님
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
            
        # 갱신을 seq[i] 만큼 수행 
        i += seq[i]
        
    return True


def count_beautiful_seq(cnt):
    global answer
    
    if cnt == n + 1:
        if is_beautiful():
            answer += 1
        return
	
    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()


count_beautiful_seq(1)
print(answer)