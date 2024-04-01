def solution(n, k):
    answer = []
    for i in range(n):
        if (i+1)*k <= n:
            answer.append((i+1)*k)
        else :
            break
    return answer
