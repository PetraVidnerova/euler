import prime
import itertools

def to_int(tuple):
    res = 0
    for i in tuple:
        res = res*10+int(i) 
    return res

def get_permutations(x):
    """
    Returns list of integers, 
    all digit permutations of integer x.
    """
    str_x = str(x)
    return [ to_int(tuple) for tuple in itertools.permutations(str_x) ] 

def is_sequence(x):
    """
    Checks if list x is arithmetic sequence.
    """ 
    x = sorted(x)
    diff = x[1] - x[0]
    for  i in range(1,len(x)-1):
        if (x[i+1]-x[i]) != diff:
            return False
    return True

def contain_sequence(x):
    """
    Returns sequence if x contains it,
    empty list otherwise.
    """
    for triple in itertools.combinations(x,3):
        if is_sequence(triple):
            return triple
    return []
                
    
for x in range(1000,9999):
    perms = get_permutations(x)
    seq = contain_sequence(perms)
    if not seq: continue
    if seq[0] == seq[1]:
        continue
    if seq[0]<1000 or seq[1]<1000 or seq[2]<1000:
        continue
    if prime.is_prime(seq[0]) and prime.is_prime(seq[1]) and prime.is_prime(seq[2]):
        print(seq)

