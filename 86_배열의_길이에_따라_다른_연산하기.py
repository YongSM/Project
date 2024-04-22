def solution(arr, n):
    answer = []
    l = len(arr)
    for i in range(l):
        if l%2 == 0 :
            if i%2 == 1 :
                arr[i] = arr[i] + n
        else :
            if i%2 == 0 :
                arr[i] = arr[i] + n
    return arr
