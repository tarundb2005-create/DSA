def greedy(g,s):
    s.sort()
    g.sort()
    i = 0
    j = 0
    count = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count
g = [1, 2, 3]
s = [1, 1, 2]
print(greedy(g,s))
