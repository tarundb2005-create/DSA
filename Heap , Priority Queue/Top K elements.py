import heapq
nums = [7, 2, 9, 4, 1, 6]
K = 3

def heapp(nums , K):
    heap = []
    for num in nums:
        heapq.heappush(heap,-num)
        if len(heap) > K:
            heapq.heappop(heap)
    result = [-x for x in heap]
    return result
print(heapp(nums , K))
