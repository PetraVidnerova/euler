import math 

target = 600851475143
factors = [] 

i=3
while i <= target:
    if target % i == 0: 
        factors.append(i) 
        target /= i 
    i += 1 

print(factors) 

max_factor = max(factors) 

primers = [True]*(max_factor+1)
 
for i in range(2,max_factor+1):
    x = 2*i
    while x<=max_factor:
        primers[x] = False
        x += i 

for x in factors:
    if primers[x]:
        print(x) 

print(primers[:30])

