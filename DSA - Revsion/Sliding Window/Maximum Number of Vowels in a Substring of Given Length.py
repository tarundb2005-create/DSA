def check(s , k):
    count = 0
    maxi = 0
    for i in range(k):
        if s[i] in "aeiou":
            count += 1
    maxi = count
    for i in range(k,len(s)):
        if s[i] in "aeiou":
            count += 1
        if s[i-k] in "aeiou":
            count -= 1
        maxi = max(maxi , count)
        
        
    return maxi
    
s = "abciiidef"
k = 3
print(check(s , k))
