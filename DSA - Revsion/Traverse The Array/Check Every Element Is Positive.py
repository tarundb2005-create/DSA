def isPositive(nums):
    res = None
    for i in range(len(nums)):
        if nums[i] <= 0:
            return False
    return True
nums = [1,2,3]
print(isPositive(nums))
