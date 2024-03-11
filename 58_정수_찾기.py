def solution(num_list, n):
    answer = 0
    l = len(num_list)
    for i in range(l):
        if num_list[i] == n:
            answer = 1
    return answer
