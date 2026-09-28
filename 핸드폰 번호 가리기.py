def solution(phone_number):
    answer = ''
    num = len(phone_number) - 4
    for i in range(num):
        answer += "*"
    for i in range(4):
        answer += phone_number[num + i]
    return answer