import math

def sum_of_powers(x):
    sum = 0
    for digit in str(x):
        sum += math.pow(int(digit),5)
    return sum 

sum = 0
for i in range(2,1000000):
    if i == sum_of_powers(i):
        print(i) 
        sum += i

print("sum:",sum)
