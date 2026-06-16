
arr = [-4,-1,0,3,10]
left = 0
right = len(arr)-1

result = [0]*len(arr)
pos = len(arr)-1

while left <= right:
    left_square = arr[left]**2
    right_square = arr[right]**2

    if left_square > right_square:
        result[pos] = left_square
        left += 1
    else:
        result[pos] = right_square
        right -= 1
    pos -= 1
print(result)
