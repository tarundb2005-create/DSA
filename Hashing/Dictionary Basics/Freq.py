arr = [1, 2, 1, 3, 2, 1]
freq = {}
for nums in arr:
    freq[nums] = freq.get(nums,0) + 1
print(freq)
