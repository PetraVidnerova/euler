def  is_primer(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True 


def prime_factors(x): 
    """
    Returns prime factors of x.
    """
    factors = [] 
    for i in range(2,x+1):
        count = 0
        while x % i == 0:
            count += 1 
            x /= i
        if count > 0:
            factors.append((i,count))
    return factors

def add(d,c):
    """
    Add to p_factors divisor d with count c.
    """
    global p_factors
    for (x,y) in p_factors:
        if x == d:
            if c > y:
                p_factors.append((d,c))
                p_factors.remove((x,y))
            return 
    p_factors.append((d,c))

def add_factors(factors):
    """
    Add to p_factors what is not there.
    """ 
    global p_factors
    for (d,c) in factors:
        add(d,c) 

p_factors = [] 
for i in range(2,21):
    add_factors(prime_factors(i)) 


print(p_factors)
x = 1
for (i,count) in p_factors:
    for j in range(count):
        x *= i
print(x)
