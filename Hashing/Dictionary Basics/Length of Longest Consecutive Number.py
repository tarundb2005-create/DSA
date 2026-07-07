def Longs(nums):
    seen = set(nums)
    longest = 0
    for num in seen:
        if num -1 not in seen:
            length = 1
            while num + length in seen:
                length += 1
            longest = max(longest,length)
    return longest
nums = [0,1,2,3,6]
print(Longs(nums))
