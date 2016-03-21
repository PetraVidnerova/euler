import itertools
import math

def  is_prime(x):
    if (x == 1):
        return False
    for i in range(2,int(math.sqrt(abs(x)))+1):
        if x % i == 0:
            return False
    return True 

def list2number(x):
    number = x[0]
    i = 1
    while i<len(x):
        number = number*10+x[i]
        i += 1 
    return number  

max = None
for n in range(4,10):
    list = [ x for x in range(1,n+1) ] 
    for x in itertools.permutations(list):
        num_x = list2number(x)
        if is_prime(num_x):
            print(num_x, max)
            if max == None or num_x > max:
                max = num_x
            
print("Max",max)
    

      
