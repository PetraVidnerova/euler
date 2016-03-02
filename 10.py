max = 2000000

primes = [True]*max

for i in range(2,max):
    x = 2*i
    while x < max:
        primes[x] = False
        x += i

sum = 0 
for i in range(2,max):
    if primes[i]: 
        sum += i 

print(sum)
