def Large(nums):
    res = 0
    for i in range(len(nums)):
        if nums[i] > nums[res]:
            res = i
    return res
        
nums = [5, 2, 9, 7]
print(Large(nums))
