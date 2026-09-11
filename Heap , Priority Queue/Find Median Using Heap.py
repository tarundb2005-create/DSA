import heapq
def medianheap(nums):
    min_heap = []
    max_heap = []

    for num in nums:
        #add the elements
        
        if not max_heap:
            heapq.heappush(max_heap,-num)
        elif num <= -max_heap[0]:
            heapq.heappush(max_heap , -num)
        else:
            heapq.heappush(min_heap , num)

        #balancing the heap
            
        if len(max_heap) > len(min_heap)+1:
            heapq.heappush(min_heap , -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap)+1:
            heapq.heappush(max_heap ,-heapq.heappop(min_heap))

    #find median
    if len(max_heap) > len(min_heap):
        return -max_heap[0]
    elif len(min_heap) > len(max_heap):
        return min_heap[0]
    else:
        return (-max_heap[0] + min_heap[0])/2
nums = [1,2,3,4,5,6]
print(medianheap(nums))
