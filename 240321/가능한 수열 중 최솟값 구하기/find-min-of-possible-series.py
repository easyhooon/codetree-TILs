import sys

si = sys.stdin.readline 

n = int(si())
numbers = [4, 5, 6]

series = []


def is_possible_series():
    for idx in range(len(series)):
        length = 1
        while True:
            # start1, end1 = idx, idx + length - 1
            # start2, end2 = end1 + 1, (end1 + 1) + length - 1

            # if end2 >= len(series):
            #     break
            start1, end1 = len(series) - length, len(series) - 1
            start2, end2 = start1 - length, start1 - 1

            if start2 < 0:
                break
            
            if series[start1: end1 + 1] == series[start2: end2 + 1]:
                return False

            length += 1

        return True

def find_min_series(cnt):
    if cnt == n:
        # if not is_possible_series():
        #     return
        
        # 가장 먼저 나오는 조합을 출력하고 프로그램 종료 
        for elem in series:
            print(elem, end = "")
        sys.exit(0)
        

    for number in numbers:
        series.append(number)
        if is_possible_series():
            find_min_series(cnt + 1)
        series.pop()

find_min_series(0)