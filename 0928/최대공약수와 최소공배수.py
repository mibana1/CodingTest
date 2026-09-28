def solution(n, m):
    answer = []
    if(n > m):
        x = n
        y = m
    else:
        x = m
        y = n
    num = 1
    num1 = []
    for i in range(x):
        while(x % (i + 2) == 0 and y % (i + 2) == 0):
            x = x // (i + 2)
            y = y // (i + 2)
            num1.append(i + 2)
        

    for i in range(len(num1)):
        num = num * num1[i]
    answer.append(num)
    answer.append(num * x * y)

    return answer