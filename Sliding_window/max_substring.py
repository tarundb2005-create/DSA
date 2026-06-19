
s = "abcabcbb"
left = 0
seen = set()
max_a = 0
for right in range(len(s)):
    while s[right] in seen :
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    
    max_a = max(max_a , right-left+1)
print(max_a)