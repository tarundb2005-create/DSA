import heapq

def ksmallest(nums , k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap , num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
     
    return max_heap[0]
nums = [1,2,3,4,5,6]
k = 3

print(ksmallest(nums,k))
