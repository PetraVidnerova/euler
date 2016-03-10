import math

def getSum(x):
    sum = 0 
    for digit in str(x):
        sum += math.factorial(int(digit)) 
    return sum 

sum = 0
# let's try 1000000
for i in range(3,1000000): 
    if i == getSum(i):
        sum += i 
        print(i) 

print("Sum:",sum)
