def histo(nums):
    stack =[]
    max_area = 0
    for i in range(len(nums) + 1):
        current = nums[i] if i < len(nums) else 0
        while stack and current < nums[stack[-1]]:
            top = stack.pop()
            right = i
            left = stack[-1] if stack else -1
            width = right - left - 1
            area = nums[top] * width
            max_area = max(area , max_area)

        if i < len(nums):
            stack.append(i)
    return max_area
nums = [2, 1, 5, 6, 2, 3]
print(histo(nums))
