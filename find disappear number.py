###Find All Numbers Disappeared in an Array
##Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.Find all the elements of [1, n] inclusive that do not appear in this array.Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
def find_disappear_num(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]