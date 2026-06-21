def BinarySearch(arr,targte):
    left = 0
    right =len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return left

arr = [1,2,3,4,5,6,7,9,10]
target = 8
print(BinarySearch(arr,target))
