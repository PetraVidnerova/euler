def next(n):
    """
    Get next number of the Collatz sequence.
    """
    if n == 1:
        return None
    if n % 2 == 0:
        return n // 2 
    else:
        return 3*n+1
    

max = None
starter = None
for i in range(1000000):
    n = i
    len = 0 
    # compute the len of sequence 
    while True:
        n = next(n)
        if n:
            len += 1
        else:
            break 
    print(i, len)
    # check if it is not maximal 
    if not max or len > max:
        max = len 
        starter = i

print(starter)
        
        
