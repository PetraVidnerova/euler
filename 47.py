target = 4

def prime_factors(x): 
    """
    Returns first five prime factors of x.
    """
    factors = [] 
    for i in range(2,x+1):
        count = 0
        while x % i == 0:
            count += 1 
            x /= i
        if count > 0:
            factors.append(i)
            if len(factors) > 4:
                break 
    return factors


for x in range(2,1000000):
    if x % 1000 == 0:
        print(x)
    if len(prime_factors(x)) == target:
        couple = True
        for i in range(1,target):
            if len(prime_factors(x+i)) != target:
                couple = False
        
        if couple == True:
            print(x)
            quit() 

            
        
