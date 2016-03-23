def pandigital(xs):
    if len(xs)!=10:
        return False
    for x in range(10):
        if str(x) not in xs:
            return False
    return True 
