def solution(n, numlist):
    answer = []
    l = len(numlist)
    for i in range(l):
        if numlist[i]%n == 0 :
            answer.append(numlist[i])
    return answer
