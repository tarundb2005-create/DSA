def koko(piles , h):
    low = 0
    high = max(piles)
    while low < high:
        mid = low + (high - low) // 2

        total = 0
        for pile in piles:
            total += (pile + mid - 1) // mid
        if total <= h:
            high = mid
        else:
            low = mid + 1
    return low
piles = [3, 6, 7, 11]
h = 8
print(koko(piles , h))
