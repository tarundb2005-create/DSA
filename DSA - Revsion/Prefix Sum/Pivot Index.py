def prefix(nums):
    prefix = [0]*len(nums)
    prefix[0] = nums[0]
    for i in range(1 , len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix

def pivot(prefix , nums):
    total = prefix[-1]
    for i in range(len(nums)):
        if i == 0:
            leftsum = 0
        else:
            leftsum = prefix[i-1]
        rightsum = total - leftsum - nums[i]

        if leftsum == rightsum:
            return i
    return -1
nums = [1, 7, 3, 6, 5, 6]
pre = prefix(nums)

print("Current Index or Pivot : ",pivot(pre,nums))
