def solution(numbers):
    answer = 0
    sum = 0
    n = len(numbers)
    for i in range(n):
        sum = sum + numbers[i]
        answer = sum / n
    return answer
