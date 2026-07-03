def Binary(arr,left,right,target):
    
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return (Binary(arr,mid + 1,right,target))
    else:
        return (Binary(arr,left,mid -1,target))
     
arr = [1,2,3,4,5,6,7]

print(Binary(arr,0,len(arr)-1,7))
