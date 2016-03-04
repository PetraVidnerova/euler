import math 

def  is_prime(x):
    for i in range(2,int(math.sqrt(abs(x)))+1):
        if x % i == 0:
            return False
    return True 


def prime_sequence_len(a,b):
    i = 0
    while is_prime(i*i+a*i+b):
        i += 1 
    return i


max = None
max_a = None
max_b = None

for a in range(-999,1000):
    for b in range(-999,1000):
        len = prime_sequence_len(a,b)
        if max == None or len > max:
            max = len
            max_a = a
            max_b = b

print(max_a*max_b)
