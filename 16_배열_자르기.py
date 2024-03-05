def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, 1+num2):
        answer.append(numbers[i])
    return answer
