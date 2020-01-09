### find number of consecutive 1 in given array
def find_consecutive_one(nums):
    local = maximum = 0
    for i in nums:
        if i == 1:
            local += 1
        else:
            local = 0
        maximum = max(maximum, local)
    return maximum