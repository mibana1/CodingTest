def solution(arr1, arr2):
    answer = [[]]
    num1 = len(arr1)
    num2 = len(arr1[0])
    answer = [[0 for col in range(num2)] for row in range(num1)]
    for i in range(num1):
        for j in range(num2):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer