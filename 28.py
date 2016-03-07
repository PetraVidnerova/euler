import numpy as np

n = 1001
spiral = np.zeros((n,n))
#start in the middle
x = (n // 2)  
y = x

direction = "right"
 
i = 1
while x < n and y < n and x >= 0 and y >= 0:
    spiral[x,y] = i 
    i += 1 
    if direction == "right": 
        y = y + 1
        if x+1 < n and y < n and spiral[x+1, y] == 0:
            direction = "down"
    elif direction == "down":
        x = x + 1 
        if y-1 >= 0 and x < n and spiral[x, y-1] == 0:
            direction = "left"
    elif direction == "left":
        y = y -1 
        if x-1 >= 0 and y >= 0 and spiral[x-1, y] == 0:
            direction = "up" 
    elif direction == "up": 
        x = x - 1
        if y+1 < n and x >= 0 and spiral[x, y+1] == 0:
            direction = "right"


sum1 = sum(spiral.diagonal()) 
sum2 = sum(spiral[::-1,:].diagonal())
print(sum1+sum2-1)
