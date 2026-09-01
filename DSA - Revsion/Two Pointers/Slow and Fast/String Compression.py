def nomo(chars):
    slow = 0
    fast = 0
    while fast < len(chars):
        current = chars[fast]
        count = 0
        while fast < len(chars) and chars[fast] == current:
            fast += 1
            count += 1
        chars[slow] = current
        slow += 1
        if count > 1:
            for i in str(count):
                chars[slow] = i
                slow += 1
    return slow
chars = ["a","a","b","b","c","c","c"]
print(nomo(chars))
