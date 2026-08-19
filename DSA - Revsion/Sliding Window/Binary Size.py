def atmost(nums , goal):
    left = 0
    curr = 0
    answer = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > goal:
            curr -= nums[left]
            left += 1
        answer += right - left + 1
    return answer
def subarray(nums , goal):
    return atmost(nums , goal) - atmost(nums , goal -1)
nums = [1,0,1,0,1]
goal = 2
print(subarray(nums , goal))
