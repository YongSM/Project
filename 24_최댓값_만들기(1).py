def solution(numbers):
    answer = 0
    n = len(numbers)
    for i in range(n):
        for l in range(n):
                if i != l:
                    if numbers[i] * numbers[l] > answer :
                        answer = numbers[i] * numbers[l]
    return answer
