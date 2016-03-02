import math 
for i in range(1000):
    for j in range(1000):
        c = math.sqrt(i*i + j*j)
        if i+j+c == 1000:
            print(i*j*c) 
    
