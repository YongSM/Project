def solution(arr, k):
    answer = []
    n = len(arr)
    for i in range(n):
        if k%2 == 1 :
            answer.append(arr[i]*k)
        else :
            answer.append(arr[i]+k)
    return answer
