def solution(num_list):
    n = len(num_list)
    if n>10 :
        answer = sum(num_list)
    else :
        answer = 1
        for i in range(n):
            answer *= num_list[i]
    return answer
