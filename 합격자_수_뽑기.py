def count_passer(score, c):
    answer = 0
    n = len(score) #어떤 길이의 자료도 소화할 수 있게
    for i in range(n):
        if score[i] >= c:
            answer += 1
    return answer


#[80, 40, 90, 55, 94, 30, 60, 44]
print(count_passer([80, 40, 90, 55, 94, 30, 60, 44], 60))
print(count_passer([20, 50, 80, 45], 60))
