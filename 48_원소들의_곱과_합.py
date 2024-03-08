def solution(num_list):
    n = len(num_list)
    a = 1
    b = 0
    for i in range(n):
        a *= num_list[i]
    b = sum(num_list)**2
    if a < b :
        answer = 1
    else  :
        answer = 0
    return answer
