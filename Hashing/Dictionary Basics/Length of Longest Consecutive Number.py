def Longs(nums):
    seen = set(nums)
    longest = 0
    for num in nums:
        if num -1 is not seen:
            length = 1
            while num + length in seen:
                length += 1
            longest = max(longest,length)
    return longest
nums = [1,2,6]
print(Longs(nums))
