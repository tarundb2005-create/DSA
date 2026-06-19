
arr = [1,3,2,6,-1,4,1,8,2]
k = 5
window_sum = sum(arr[:k])
avg_a = []
for i in range(k,len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    avg_a.append(window_sum/k)
print(avg_a)
