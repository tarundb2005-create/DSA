def binary(nums , target):
    left = 0
    right = len(nums)-1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
nums   = [1, 2, 2, 4, 5, 7]
target = 2
print(binary(nums, target))
