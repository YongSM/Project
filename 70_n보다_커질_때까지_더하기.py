def solution(numbers, n):
    answer = 0
    l = len(numbers)
    for i in range(n):
        answer += numbers[i]
        if answer > n:
            break
    if answer == 0 :
        answer = numbers[0]
    return answer
