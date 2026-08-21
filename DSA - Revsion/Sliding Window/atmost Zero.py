def oddd(nums,k):
    left = 0
    odd_count = 0
    answer = 0
    for right in range(len(nums)):
        if nums[right]%2 == 1:
            odd_count += 1

        while odd_count > k:

            if nums[left] % 2 == 1:
                odd_count -= 1
            left += 1
        answer += right - left + 1
    return answer
def atmost(nums,k):
    return oddd(nums , k) - oddd(nums , k-1)

nums = [1, 2, 1, 1, 2]
k = 2
print(atmost(nums,k))
