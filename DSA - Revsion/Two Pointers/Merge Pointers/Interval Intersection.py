nums1 = [[0,2],[5,10],[13,23],[24,25]]
nums2 = [[1,5],[8,12],[15,24],[25,26]]

i = 0
j = 0
result = []
while i < len(nums1) and j < len(nums2):
    start = max(nums1[i][0] , nums2[j][0])
    end = min(nums1[i][1], nums2[j][1])

    if start <= end:
        result.append([start,end])
    if nums1[i][1] < nums2[j][1]:
        i += 1
    else:
        j += 1

print(result)
