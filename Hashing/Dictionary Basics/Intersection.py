def inter(nums1,nums2):
    seen = set(nums1)
    result = set()
    for num in nums2:
        if num in seen:
            result.add(num)
    return result
nums1 = [1,2,3]
nums2 = [1,2,4]
print(inter(nums1,nums2))
