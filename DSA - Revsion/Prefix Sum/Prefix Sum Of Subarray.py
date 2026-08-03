
def sumsub(nums, k):
    count = 0
    hashmap = {0: 1}
    prefix = 0

    for i in range(len(nums)):
        prefix += nums[i]

        if prefix - k in hashmap:
            count += hashmap.get(prefix - k)

        hashmap[prefix] = hashmap.get(prefix, 0) + 1

    return count
