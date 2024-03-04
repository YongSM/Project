def minimum_value(nums):
    answer = 0
    min_n = 100000
    n = len(nums) 
    #print(n) 
    for i in range(n):
        if nums[i] < min_n:
            min_n = nums[i]
            #print(min_n)
            answer = i
    return answer

print(minimum_value([23, 20, 73, 98, 11, 4, 288]))
print(minimum_value([33, 423, 32, 2, 56]))
print(minimum_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
