def solution(sides):
    answer = 2
    if (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[0] + sides[2] > sides[1])  :
        answer = 1
    return answer
