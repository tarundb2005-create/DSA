def nextsmallest(nums):
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] <= nums[i] :
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    return result
nums = [3, 7, 1, 8, 4, 6]

print(nextsmallest(nums))
