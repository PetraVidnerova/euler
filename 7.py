max = 1000000
primes = [True]*max

for i in range(2,max):
    x = 2*i
    while x < max:
        primes[x] = False
        x += i

print(primes[:30])
count = 1
x = 2
while count < 10001:
    x += 1 
    if primes[x]:
        count += 1

print(x)
