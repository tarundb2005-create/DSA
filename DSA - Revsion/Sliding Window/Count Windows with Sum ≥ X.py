def addele(nums , k , x):
    curr = 0
    count = 0
    for i in range(k):
        curr += nums[i]
        if curr >= x:
            count += 1
    for i in range(k , len(nums)):
        curr += nums[i]
        curr -= nums[k-i]
        if curr >= x:
            count += 1
    return count
nums = [2, 1, 5, 1, 3, 2]
k = 3
x = 6
print(addele(nums , k , x))
    
