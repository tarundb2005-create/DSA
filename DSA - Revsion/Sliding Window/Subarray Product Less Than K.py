def maximize(nums , goal):
    left = 0
    answer = 0
    product = 1
    for right in range(len(nums)):
        product *= nums[right]

        while product >= goal:
            product //= nums[left]
            left += 1
        answer += right - left + 1
    return answer
nums = [10, 5, 2, 6]
goal = 100
print(maximize(nums,goal))
