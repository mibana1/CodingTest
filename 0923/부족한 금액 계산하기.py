def solution(price, money, count):
    answer = 0
    num = 0
    for i in range(count):
        num += price * (i + 1)
        if(money - num < 0):
            answer = num - money
        else:
            answer = 0
    return answer