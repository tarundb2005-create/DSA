def reverse(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    return reverse(arr,left + 1,right - 1)
arr = [10,20,30,40,50]
reverse(arr,0,len(arr)-1)
print(arr)
