primes = [True]*1000001
for i in range(2,1000000):
    j = 2*i
    while (j<1000000):
        primes[j] = False
        j += i


def rotated(x):
    '''
    Returns list of all rotations of digits.
    '''
    ret = []
    xs = str(x) 
    for i in range(len(xs)):
        rotated = int(xs[i:]+xs[:i])
        ret.append(rotated) 
    return ret 


def circular(x):
    for x in rotated(x):
        if not primes[x]:
            return False
    return True

num_circular = 0
for i in range(2,1000000):
    if primes[i] and circular(i):
        print(i)
        num_circular += 1 
                

print("Number:",num_circular)
