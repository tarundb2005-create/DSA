def prefix(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix
def leftandrightsum(prefix , nums):
    total = prefix[-1]
    ans = []
    for i in range(len(nums)):
        if i == 0:
            left = 0
        else:
            left = prefix[i-1]
        right = total - left - nums[i]
        ans.append(abs(left - right))
    return ans
nums = [10, 4, 8, 3]
pre = prefix(nums)
ref = leftandrightsum(pre,nums)
print(nums)
print(pre)
print(ref)
