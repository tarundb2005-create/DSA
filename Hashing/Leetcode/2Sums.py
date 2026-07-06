def twosum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hashmap:
            return [hashmap[comp],i]
        hashmap[nums[i]] = i
nums = [2, 7, 11, 15]
target = 18
print(twosum(nums,target))
