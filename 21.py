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


def amicable(x):
    y = sum_factors(x)
    xx = sum_factors(y)
    print(x,y,xx)
    if xx == x and y != x:
        return True
    return False


sumam = 0
for x in range(2,10001):
    if amicable(x):
        sumam += x

print(sumam)
