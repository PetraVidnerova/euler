import math 

target = 600851475143
target_factors = [] 

# find all divisors of target 
for i in range(2,int(math.sqrt(target))+1):
    x = 2*i
    while x < target:
        x += i 
    if x == target:
        target_factors.append(i) 

# delete those who are primes 
for i in range(2,int(math.sqrt(target))+1):
    x = 2*i
    while x < target:
        if x in target_factors:
            target_factors.remove(x) 
        x += i 

print(target_factors)

        
