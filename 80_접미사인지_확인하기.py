def solution(my_string, is_suffix):
    answer = 0
    n = len(my_string)
    for i in range(n):
        if my_string[i:] == is_suffix:
            answer=1 
    return answer
