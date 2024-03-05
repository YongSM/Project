def solution(array, height):
    answer = 0
    n = len(array)
    for i in range(n):
        if array[i] > height:
            answer += 1
    return answer
