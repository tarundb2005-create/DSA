def ano(s):
    seen = {}
    for i in s:
        key = "".join(sorted(i))

        if key not in seen:
            seen[key] = []
        seen[key].append(i)
    return list(seen.values())
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(ano(s))
