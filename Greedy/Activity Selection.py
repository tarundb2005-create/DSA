def greedy(activity):
    activity.sort(key=lambda x:x[1])
    count = 0
    last_end = 0
    for start , end in activity:
        if start >= last_end:
            count += 1
            last_end = end
    return count
activity = [
    (1, 2),
    (3, 4),
    (0, 6),
    (5, 7),
    (8, 9),
    (5, 9)
]
print(greedy(activity))
