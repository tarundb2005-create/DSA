import heapq

def greed(lists):
    lists.sort(key = lambda x:x[1])
    max_heap = []
    total_time = 0
    for duration , deadline in lists:
        heapq.heappush(max_heap , -duration)
        total_time += duration
        if total_time > deadline:
            remove = heapq.heappop(max_heap)
            total_time += remove
    return len(max_heap)
lists = [
    [1, 2],
    [2, 2],
    [1, 3]
]

print(greed(lists))
