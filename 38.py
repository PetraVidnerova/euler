def pandigital(xs):
    if '0' in xs:
        return False
    if len(xs)!=9:
        return False
    for x in range(1,10):
        once = False
        for c in xs:
            if str(x) == c:
                if not once:
                    once = True 
                else:
                    return False 
        if not once:
            return False
    return True 


for x in range(9999):
    for n in range(2,9):
        soucet = ""
        for i in range(1,n+1):
            soucet = soucet + str(x*i)
        if pandigital(soucet):
            print(soucet)
