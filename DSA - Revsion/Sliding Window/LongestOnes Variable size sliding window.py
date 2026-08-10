def maxii(nums , k):
    left = 0
    maxi = 0
    zero = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero += 1
        while zero > k:
            if nums[left] == 0:
                zero -= 1
            left += 1
        maxi = max(maxi , right - left +1)
    return maxi
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(maxii(nums,k))
