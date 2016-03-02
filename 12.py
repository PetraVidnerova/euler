import math 

def factors_count(x):
    factors = [1]
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            factors.append(i)
            factors.append(x // i)
    factors.append(x)
    return len(set(factors))

def triangular(n):
    return sum(range(n+1)) 

i = 10
while True:
    t = triangular(i)
    if factors_count(t) > 500:
        print(t) 
        break
    i += 1 
