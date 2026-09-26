def greedy(nums):
    farthest = 0
    for i in range(len(nums)):
        
        if i > farthest:
            return False
        farthest = max(farthest , i + nums[i])
        if farthest >= len(nums)-1:
            return True
    return True
nums = [3 , 3, 1, 1, 4]
print(greedy(nums))
