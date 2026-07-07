def happy(n):
    #lets have list called seen where the number is already present
    seen = set()
    #edge case
    while n != 1:
        #check n is already in seen 
        if n in seen:
            #if it return false
            return False
        seen.add(n) # Mark this number as visited
        total = 0 # Stores the sum of squares of digits
        while n > 0: #the input number should be greater than 0
            digit = n % 10
            #upadate the the square values is total
            total += digit * digit
            n//= 10
        n = total
    return True
n = 12
print(happy(n))
