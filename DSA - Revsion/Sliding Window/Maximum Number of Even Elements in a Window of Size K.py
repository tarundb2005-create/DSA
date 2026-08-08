def maxeve(nums , k):
    count = 0
    maxi = 0
    curr = 0
    for i in range(k):
        if nums[i] % 2 == 0:
            count += 1
    maxi = count
    for i in range(k,len(nums)):
        if nums[i] % 2 == 0:
            count += 1
        if nums[i-k] % 2 == 0:
            count -= 1
        maxi = max(maxi , count)
    return maxi
nums = [1, 2, 4, 7, 6, 8, 2]
k = 3
print(maxeve(nums,k))
