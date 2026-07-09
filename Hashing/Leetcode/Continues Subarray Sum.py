#the continues sum have to divisible by k and remainder should be 0
def pre(nums):
    prefix = 0
    hashmap = {0:-1}    # edge case (0:-1)
    for i in range(len(nums)):
        prefix += nums[i]
        remainder = prefix % k
        if remainder in hashmap:
            if i - hashmap[remainder] >= 2:   # the value should be more than or equal 2
                return True
        if remainder not in hashmap:
            hashmap[remainder] = i
    return False
nums = [2,4]
k = 6
print(pre(nums))
