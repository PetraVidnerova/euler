import itertools
import functools

def divisibility(xs):
    divisors = [ 2, 3, 5, 7, 11, 13, 17] 
    for i in range(len(divisors)):
        if int(xs[1+i:4+i]) % divisors[i] != 0:
            return False
    return True


digits = "0123456789"
total = 0 
for x in itertools.permutations(digits):
    if x[0] == '0':
        continue
    xs = functools.reduce(lambda a,b: a+b,x)
    if divisibility(xs):
        total += int(xs) 

print(total)
