def solution(arr1, arr2):
    answer = 0
    n1 = len(arr1)
    n2 = len(arr2)
    L1 = 0
    L2 = 0
    if n1 == n2 :
        for i in range(n1):
            L1 += arr1[i]
            L2 += arr2[i]
        if L1 > L2 :
            answer = 1 
        elif L2 > L1 :
            answer = -1
        else :
            answer = 0
    elif n1 > n2 :
        answer = 1
    elif n1 < n2 :
        answer = -1
    return answer
