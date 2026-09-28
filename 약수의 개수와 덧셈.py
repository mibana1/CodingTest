def solution(left, right):
    answer = 0
    num = 0
    for i in range(right - left + 1):
        for j in range(left + i):
            if((left + i) % (j + 1) == 0):
                num += 1
        if(num % 2 == 0):
            answer += left + i
        else:
            answer -= left + i
        num = 0
    return answer