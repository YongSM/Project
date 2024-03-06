def solution(n):
    a = n%10
    b = (n%100)//10
    c = (n%1000)//100
    d = (n%10000)//1000
    e = (n%100000)//10000
    f = (n%1000000)//100000
    g = (n%10000000)//1000000
    answer = a+b+c+d+e+f+g
    return answer
