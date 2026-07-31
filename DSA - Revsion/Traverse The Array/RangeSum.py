def prefix(nums):
    prefix = [0]*len(nums)
    prefix[0] = nums[0]
    for i in range(1 , len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix

def rangesum(prefix,left,right):
    for i in range(left , right):
        if left == 0:
            return prefix[right]
    return prefix[right] - prefix[left-1]
nums = [1, 2, 3, 4, 5, 6]
left = 2
right = 4
prefix = prefix(nums)
print(rangesum(prefix,left,right))
