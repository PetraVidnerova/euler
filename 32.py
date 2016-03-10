def isPandigital(x,y): 
    digits=str(x)+str(y)+str(x*y)
    if '0' in digits:
        return False
    for i in range(1,10):
        once = False
        si = str(i)
        for x in digits:
            if si == x:
                if once: # more same digits
                    return False
                else: # first occurance 
                    once = True 
        if not once: #no occurence of i 
            return False
    return True 

print(isPandigital(39,186)) 

products = set() 
for x in range(999):
    for y in range(9999):
        if isPandigital(x,y):
            products.add(x*y)

print(sum(products))
