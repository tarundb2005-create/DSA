def no(nums1,nums2,m,n):
    i = m - 1
    j = n - 1
    write = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1
    while j > 0:
        nums1[write] = nums2[j]
        j -= 1
        write -= 1
    return nums1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(no(nums1,nums2,m,n))
