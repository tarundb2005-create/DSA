##nums = [1, 12, -5, -6, 50, 3]
##k = 4
##
##Output:
##12.75
        
def MaxAvg(nums , k):
    curr = 0
    avg = 0
    maxi = 0
    for i in range(k):
        curr += nums[i]
    avg = curr / k
    maxi = avg
    for i in range(k,len(nums)):
        curr += nums[i]
        curr -= nums[i-k]
        avg = curr /k
        maxi = max(maxi ,avg)
    return maxi

nums = [5]
k = 1
print(MaxAvg(nums,k))
