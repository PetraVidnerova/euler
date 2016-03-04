import math

def get_factors(x):
    factors = [1]
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            factors.append(i)
            j = x // i 
            if j != i:
                factors.append(j)
    return factors

def sum_factors(x):
    return sum(get_factors(x))

abundant = set()
for i in range(2,28124):
    if i < sum_factors(i):
        abundant.add(i) 

def is_sum(x):
    global abundant
    for i in range(2, x):
        if i in abundant and (x-i) in abundant:
            return True
    return False



total = 1
for i in range(2,28124):
    if is_sum(i): continue
    total += i

print(total)
