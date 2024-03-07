def solution(my_string):
    answer = 0
    n = len(my_string)
    for i in range(n):
        if my_string[i].isdigit():
            answer += int (my_string[i])
    return answer
