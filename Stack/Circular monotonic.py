def mono(nums):
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums)*2):
        index = i % len(nums)
        while stack and nums[index] > nums[stack[-1]]:
            result[stack.pop()] = nums[index]
        if i < len(nums):
            stack.append(index)
    return result

nums = [2, 1, 5, 3, 4]

print(mono(nums))
