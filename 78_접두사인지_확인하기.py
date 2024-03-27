def solution(my_string, is_prefix):
    answer = 1
    n = len(is_prefix)
    l = len(my_string)
    if n>l :
        answer = 0
    else :
        for i in range(n-1):
            if my_string[i] != is_prefix[i] :
                answer = 0
    return answer
