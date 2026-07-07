def Majority(nums):
    frq = {}
    for num in nums:
        frq[num] = frq.get(num,0) + 1
    for key,value in frq.items():
        if value > len(nums)//2:
            return key
    
nums = [1,2,3,3,3]
print(Majority(nums))
