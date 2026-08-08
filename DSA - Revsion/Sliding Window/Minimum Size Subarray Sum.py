def tar(nums , target):
    left = 0
    curr = 0
    answer = float('inf')
    for right in range(len(nums)):
        curr += nums[right]
        while curr >= target:
            answer = min(answer , right - left + 1)
            curr -= nums[left]
            left += 1
    if answer == float('inf'):
        return 0
    return answer
nums = [ 2 , 3 ,1 , 2 , 4 ,3]
target = 7
print(tar(nums,target))
