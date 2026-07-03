def Fibbo(n):
    if n < 2:
        return n
    return Fibbo(n-1) + Fibbo(n - 2)
    
print(Fibbo(7))
    
