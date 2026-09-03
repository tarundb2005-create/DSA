class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i = 0
        j = 0
        result = []

        total = len(nums1) + len(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        if total % 2 == 1:
            return float(result[total // 2])
        else:
            middle = total // 2
            return (result[middle - 1] + result[middle]) / 2
