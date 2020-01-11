###plus one: Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.You may assume the integer do not contain any leading zero, except the number 0 itself.The digits are stored such that the most significant digit is at the head of the list.
def plus_one(nums):
    add = 1
    for i in range(len(nums)-1, -1, -1):
        nums[i] += add
        if nums[i] == 10:
            nums[i] == 0
            if i == 0:
                nums.insert(0,1)
        else:
            break
    return nums       