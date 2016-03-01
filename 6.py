import itertools 

numbers = [ x for x in range(1,101) ]

sum = 0 
for x,y in itertools.combinations(numbers,2):
    sum += x*y 

print(2*sum)
