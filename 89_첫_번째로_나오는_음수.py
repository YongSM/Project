def solution(num_list):
    answer = -1
    n = len(num_list)
    for i in range(n):
        if num_list[i] < 0 :
            answer = i
            break;
    return answer
