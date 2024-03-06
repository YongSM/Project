# 문제 4 Range advanced
# 1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
answer = []
n = len(numbers)
def solution(numbers):
    for i in range(n):
        if numbers[i]%2 == 0:
            answer.append(numbers[i]*10)
        else :
            answer.append(numbers[i])
    return answer

print(solution(numbers))
