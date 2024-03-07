def solution(my_string):
    mo = ("a,e,i,o,u")
    answer = ''
    for i in mo:
        my_string = my_string.replace(i,"")
    return my_string
