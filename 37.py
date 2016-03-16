import math

def  is_prime(x):
    if (x == 1):
        return False
    for i in range(2,int(math.sqrt(abs(x)))+1):
        if x % i == 0:
            return False
    return True 


def truncatable(x):
    sx = str(x) 
    for i in range(len(sx)):
        if not is_prime(int(sx[i:])):
            return False
        if not is_prime(int(sx[:len(sx)-i])):
            return False
    return True

i = 10	   
num = 0	   
sum = 0	   
while num < 11:
    if truncatable(i):
        print(i)
        sum += i
        num += 1   	    
    i+=1 

print(sum)
