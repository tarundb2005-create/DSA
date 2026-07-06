def FD(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False    
    
nums = [2,2,7, 11, 15]

print(FD(nums))
