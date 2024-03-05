def solution(strlist):
    answer = []
    n = len(strlist)
    for i in range(n):
        answer.append(len(strlist[i]))
    return answer
