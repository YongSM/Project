def solution(my_string, n):
    answer = []
    l = len(my_string)
    for i in range(l):
        for j in range(n):
            answer.append(my_string[i])
    answer = "".join(answer)
    return answer
