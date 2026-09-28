def solution(num):
    answer = 0
    num2 = 0
    while True:
        if(num == 1 and num2 == 0):
            answer = 0
            break
        if(num == 1 and num2 > 0):
            answer = num2
            break
        if(num % 2 == 0):
            num = num / 2
            num2 += 1
        else:
            num = (num * 3) + 1
            num2 += 1
        if(num2 >= 500):
            answer = -1
            break
    return answer