def solution(n):
    answer = -1
    for i in range(n):
        if (n % (i + 1) == 0):
            if ( (i + 1) * (i + 1) == n):
                answer = (i + 2) * (i + 2)
                break
        
    return answer