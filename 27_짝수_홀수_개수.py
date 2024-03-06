def solution(num_list):
    answer = []
    n = len(num_list)
    a = 0
    b = 0
    for i in range(n):
        #if num_list[i] == 0 :
            #a = a
        if num_list[i]%2 == 0:
            a = a + 1
        elif num_list[i]%2 == 1:
            b = b + 1
    answer = [a, b]
    return answer
