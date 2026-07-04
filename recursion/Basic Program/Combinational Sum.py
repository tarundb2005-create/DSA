def ComSum(index,arr,ans,target,total):
    if total == target:
        print(ans)
        return
    if total > target:
        return
    if index == len(arr):
        return

    ans.append(arr[index])
    ComSum(index,arr,ans,target, total + arr[index])

    ans.pop()

    ComSum(index + 1,arr,ans,target,total)

arr = [2,3,4,5,6]
ComSum(0,arr,[],8,0)
