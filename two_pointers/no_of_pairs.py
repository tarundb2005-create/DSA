arr = [1,1,2,2,3,3,4,4]
left,right = 0,1 
count = 0

while right<len(arr):
    if arr[left] == arr[right]:
       count += 1
       left += 2
       right +=2
    else:
        left +=1
        right += 1
print(count)