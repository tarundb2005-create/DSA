def iso(s,t):
    map1 = {}
    map2 ={}
    for ch1,ch2 in zip(s,t):
        if ch1 in map1 and map1[ch1] != ch2:
            return False
        if ch2 in map2 and map2[ch2] != ch1:
            return False
        map1[ch1]= ch2
        map2[ch2] = ch1
    return True
s = "add"
t = "egg"
print(iso(s,t))
