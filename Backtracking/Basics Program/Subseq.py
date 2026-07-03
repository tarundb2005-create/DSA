def Sub(arr,index,ans):
    if index == len(arr):
        print(ans)
        return
    ans.append(arr[index])
    Sub(arr,index + 1,ans)

    ans.pop()

    Sub(arr,index +1 ,ans)
arr = [1,2,3]
Sub(arr,0,[])
