
arr = [1,1,2,2,3,3,4,4]

slow = 0

for fast in range(1,len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] == arr[fast]

print(arr[:slow+1])