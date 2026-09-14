def nextsmallest(nums):
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] < nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
nums = [4, 5, 2, 10, 8]

print(nextsmallest(nums))
