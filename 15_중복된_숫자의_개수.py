def solution(array, n):
    answer = 0
    a = len(array)
    for i in range(a):
        if array[i] == n:
            answer += 1
    return answer
