def mini(s , k):
    count = 0
    mini = 0
    for i in range(k):
        if s[i] in "aeiou":
            count += 1
    mini = count
    for i in range(k,len(s)):
        if s[i] in "aeiou":
            count += 1
        if s[i-k] in "aeiou":
            count -= 1
        mini = min(mini , count)
    return mini
s = "abciiidef"
k = 3
print(mini(s,k))
