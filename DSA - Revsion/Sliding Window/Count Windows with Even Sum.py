def evenwindow(nums , k):
    count = 0
    curr = 0
    for i in range(k):
        curr += nums[i]
    if curr % 2 == 0:
        count += 1
    for i in range(k,len(nums)):
        curr += nums[i]
        curr -= nums[i-k]
        if curr % 2 == 0:
            count += 1
    return count
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(evenwindow(nums,k))
