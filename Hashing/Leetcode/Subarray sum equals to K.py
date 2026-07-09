def pre(nums,k):
    count = 0
    prefix = 0
    hashmap = {0 : 1}
    for i in nums:
        

        prefix += i
        need = prefix - k
        count += hashmap.get(need,0)
        hashmap[prefix] = hashmap.get(prefix,0) + 1
    return count
nums = [1,3,2]
k = 5
print(pre(nums,k))
