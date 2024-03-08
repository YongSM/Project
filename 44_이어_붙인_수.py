def solution(num_list):
    a = '' 
    b = ''
    n = len(num_list)
    for i in range(n):
        if num_list[i]%2 == 0 :
            a += str(num_list[i])
        else :
            b += str(num_list[i])
    answer = int(a)+int(b)
    return answer
