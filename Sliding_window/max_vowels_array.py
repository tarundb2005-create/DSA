s = "abciiiidef"
k = 4
vowels = "aeiou"
count = 0
for i in s[:k]:
    if i in vowels:
        count += 1
max_count = count
for j in range(k,len(s)):
    if s[j-k] in vowels:
        count -= 1
    if s[j] in vowels:
        count += 1
    max_count = max(count,max_count)
print(max_count)
