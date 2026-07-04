def ComSum(arr,index,target,total,ans):
    if target == total:
        print(ans)
        return
    if total > target:
        return
    for i in range(index,len(arr)):
        if i > index and arr[i] == arr[i - 1]:
            continue
        ans.append(arr[i])
        ComSum(arr,i+1,target,total + arr[i],ans)
        ans.pop()
    

arr = [1,2,3,4,5,6]
target = 7
ComSum(arr,0,target,0,[])
