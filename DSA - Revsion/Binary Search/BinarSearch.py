def binary(nums , target):
    l , r = 0 , len(nums)-1
    while l <= r:
        mid = l + ( r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
nums = [1,2,3,4,5,6,7]
print(binary(nums , 0))
