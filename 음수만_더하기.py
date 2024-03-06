# 문제 1. 음수만 더해주세요
# 새로운 리스트에 음수  리스트를 출력해주세요

num_list = [1,-2,3,-4,5]
num_list2 = [3223, 42, -3, 85, -238, 68, 12]

def solution(num_list):
    answer = 0
    n = len(num_list)
    for i in range(n):
        if num_list[i] < 0 :
            answer += num_list[i]
    return answer

print(solution(num_list))
print(solution(num_list2))
