def solution(a, b):
    answer = int(str(a)+str(b))
    answer2 = int(str(b)+str(a))
    if answer2 > answer : answer = answer2
    return answer
