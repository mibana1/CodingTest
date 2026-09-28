def solution(arr):
    answer = []
    num = len(arr)
    for i in range(num - 1):
        if(arr[i] != arr[i + 1]):
            answer.append(arr[i])
    answer.append(arr[num - 1])
    return answer