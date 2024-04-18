def solution(arr):
    answer = []
    n = len(arr)
    for i in range(n):
        for l in range(int(arr[i])):
            answer.append(arr[i])
    return answer
