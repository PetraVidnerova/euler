def symetric(s):
    if s == s[::-1]:
        return True
    else:
        return False 


def palindrom10(x):
    if symetric(str(x)):
        return True
    return False 

def palindrom2(x): 
    binary = bin(x)[2:]
    if symetric(binary):
        return True
    return False 

sum = 0
for x in range(1000000):
    if palindrom10(x) and palindrom2(x):
        sum += x 

print(sum)
