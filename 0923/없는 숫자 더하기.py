def solution(numbers):
    answer = 0
    num = 0
    num2 = 0
    for i in range(10):
        for j in range(len(numbers)):
            if (i != numbers[j]):
                num += 1
            if (num == len(numbers)):
                num2 = i
        answer += num2
        num = 0
        num2 = 0
    return answer