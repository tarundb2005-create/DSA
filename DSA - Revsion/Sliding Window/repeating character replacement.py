def character(s , k):
    left = 0
    count = {}
    answer = 0
    maxf = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
        maxf = max(maxf , count[s[right]])
        while right - left + 1 - maxf > k:
            count[s[right]] -= 1
            left += 1
        answer = max(answer , right - left + 1)
    return answer
s = "aabaca"
k = 2
print(character(s,k))
