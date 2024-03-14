def solution(arr):
    answer = []
    n = len(arr)
    for i in range(n):
        if arr[i]>=50 and arr[i]%2 ==0 :
            answer.append(arr[i]/2)
        elif arr[i]<50 and arr[i]%2 ==1 :
            answer.append(arr[i]*2)
        else :
            answer.append(arr[i])
    return answer
