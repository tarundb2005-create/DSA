
arr = [1,12,-5,-6,50,3]
k = 4
window = sum(arr[:k])
max_a = window
for i in range(k,len(arr)):
    window = window - arr[i-k] + arr[i]
    max_a = max(window,max_a)
print(max_a/k)