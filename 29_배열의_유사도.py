def solution(s1, s2):
    answer = 0
    n = len(s1)
    m = len(s2)
    for i in range(n):
        for l in range(m):
            if s1[i] == s2[l]:
                answer += 1
    return answer
