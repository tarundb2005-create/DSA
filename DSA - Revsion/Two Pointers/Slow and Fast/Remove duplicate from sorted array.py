def sortnum(nums):
    slow = 0
    fast = 1
    for fast in range(len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
            
            
            

    return slow+1
nums = [0, 0, 1, 2, 2, 3, 3, 4]
print(sortnum(nums))
