###find the maximum number in given arrays, if it is more than two times of other numbers, return index. Or return -1
def find_maximum(nums):
    maximum = second = 0
    for i in range(len(nums)):
        if nums[i] > maximum:
            second = maximum
            maximum = nums[i]
            idx = i
        elif second < nums[i]:
            second = nums[i]
    return idx if maximum >= 2*second else -1
        
    
            
            
        