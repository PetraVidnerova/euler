import math 

# zero and one are not primes
primes = [False, False] 
squares = [False, True] 

def addToPrimes(x,prime):
    global primes 
    if x < len(primes):
        primes[x] = prime 
    else:
        while len(primes)<=x:
            primes.append(None)
        primes[x] = prime

def addToSquares(x, square):
    global squares
    if x < len(squares):
        squares[x] = square 
    else:
        while len(squares)<=x:
            squares.append(None)
        squares[x] = square


def  is_prime(x):
    global primes
    if x < len(primes) and primes[x] != None:
        return primes[x] 
    for i in range(2,int(math.sqrt(abs(x)))+1):
        if x % i == 0:
            addToPrimes(x, False) 
            return False
    addToPrimes(x, True) 
    return True 

def is_even(x):
    return int(x) % 2 == 0

        
def is_square(x):
    global squares
    if x < len(squares) and squares[x] != None:
        return squares[x]  
    sqrtx = math.sqrt(x) 
#    if int(sqrtx)-sqrtx < 0.00000000000001:
    if int(sqrtx)==sqrtx: 
        addToSquares(x, True)
        return True
    addToSquares(x, False)
    return False

def is_prime_and_square(x):
    for y in range(2,x):
        if is_even(x-y) and is_prime(y) and is_square((x - y) // 2):
             return True 
    return False 

#for i in range(100):
#    if is_square(i):
#        print(i)
#quit()

#for i in range(100):
#    if is_prime(i):
#        print(i)

#for i in range(50):
#    if is_prime_and_square(i):
#        print(i)
#quit()

i=3
while i<1000000:
    i += 2
    if i % 10001 == 0:
        print(i)
    if is_prime(i):
        continue
    if not is_prime_and_square(i):
        print(i)
        quit()
