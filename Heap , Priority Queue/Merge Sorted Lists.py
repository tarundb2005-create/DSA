import heapq

def mergeheap(lists):
    heap = []
    result = []
    for i , lst in enumerate(lists):
        if lst:
            heapq.heappush(heap,(lst[0] , i , 0))
    while heap:
        value , list_index , element_index = heapq.heappop(heap)
        result.append(value)
        next_index = element_index + 1
        if next_index < len(lists[list_index]):
            next_value = lists[list_index][next_index]
            heapq.heappush(heap , (next_value , list_index , next_index))
    return result
                               
            
lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print(mergeheap(lists))
