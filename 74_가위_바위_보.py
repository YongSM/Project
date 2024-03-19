def solution(rsp):
    answer = ''
    n = len(rsp)
    for i in range(n):
        if int(rsp[i]) == 2 :
            answer += str(0)
        elif int(rsp[i]) == 0 :
            answer += str(5)
        elif int(rsp[i]) == 5 :
            answer += str(2)
    return answer
