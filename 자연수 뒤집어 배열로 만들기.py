def solution(n):
    length = len(str(n))
    answer = []
    for i in range(length):
        answer.append(str(n)[i])
    answer = list(map(int, answer))
    answer.reverse()
    return answer