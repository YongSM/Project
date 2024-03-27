def solution(strArr):
    answer = []
    n = len(strArr)
    for i in range(n):
        if i%2 == 0 :
            answer.append(strArr[i].lower())
        else :
            answer.append(strArr[i].upper())
    return answer
