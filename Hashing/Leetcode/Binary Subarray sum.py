def pre(nums):
    prefix = 0
    count = 0
    hashmap = {0:1}
    for i in range(len(nums)):
        prefix += nums[i]
        need = prefix - goal
        count+= hashmap.get(need,0)
        hashmap[prefix] = hashmap.get(prefix,0)+1
    return count
nums = [1,0,1,0,1]
goal = 2
print(pre(nums))
