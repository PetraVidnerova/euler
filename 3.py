target = 13195
prime_grid = [True] * target  
target_factors = [] 
for i in range(2,target):
    x = 2*i
    while x < target:
        prime_grid[x] = False  
        x += i 
    if x == target:
        target_factors.append(i) 

for i in range(2,target):
    if prime_grid[i] and i in target_factors:
        print(i) 


