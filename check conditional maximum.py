###find the maximum number in given arrays, if it is more than two times of other numbers, return index. Or return -1
def find_maximum(nums):
    local = 0
    for i in range(len(nums)):
        if nums[i] >= local:
            local = nums[i]
    
    for j in range(len(nums)):
        if local >= 2*nums[j]:
            return i
        else:
            return -1
        
    
            
            
        