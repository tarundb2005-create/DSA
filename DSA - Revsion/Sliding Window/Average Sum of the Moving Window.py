def Avgsum(nums, k):
    curr = 0
    arr = []
    for i in range(k):
        curr += nums[i]
    arr.append(curr / k)
    for i in range(k, len(nums)):
        curr += nums[i]
        curr -= nums[i - k]
        arr.append(curr / k)
    return arr

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(Avgsum(nums, k))
