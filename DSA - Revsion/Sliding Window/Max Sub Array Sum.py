def subarray(nums,k):
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    answer = current_sum
    for i in range(k , len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        answer = max(answer , current_sum)
    return answer
nums = [1,2,3,4,5,6]
k = 3
print(subarray(nums,k))
