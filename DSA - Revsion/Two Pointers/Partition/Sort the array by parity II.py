nums = [1,2,3,4,5,6]
odd = 1
even = 0
while odd < len(nums) and even < len(nums):
    if nums[even] % 2 == 0:
            even += 2
    elif nums[odd] % 2 != 0:
            odd += 2
    else:
        nums[odd] , nums[even] = nums[even] , nums[odd]
print(nums)
        
