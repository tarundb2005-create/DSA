height = [1,8,6,2,5,4,8,3,7] 
i = 0
j = len(height)-1
res = 0
while i<j:
    area = (j - i)*min(height[i],height[j])
    res = max(res,area)
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
        
print(res)
