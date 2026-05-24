def solution(my_string, letter):
    for i in range(len(my_string)):
        if(my_string[i] != letter):
            answer += my_string[i] 
    answer = ''
    return answer