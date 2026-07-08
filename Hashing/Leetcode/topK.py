def topK(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0)+1
    sorted_item = sorted(freq.items(),key = lambda x:x[1],reverse = True)
    res = []
    for i in range(k):
        res.append(sorted_item[i][0])
    return res
nums = [1,1,2,2,2,3,3,3,3,3,3,4,4,4,4]
k = 2
print(topK(nums))
