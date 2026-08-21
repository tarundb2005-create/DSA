def twopointers(nums , k):
    left = 0
    right = len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total == k:
            return [left +1 , right+1]
        elif total > k:
            right -= 1
        else:
            left += 1
    return []
nums = [2, 7, 11, 15]
k = 9
print(twopointers(nums,k))
