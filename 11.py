import numpy as np 

def load_grid():
    grid = [] 
    for line in open("input11.txt"):
        values = line.split() 
        grid.append([x for x in map(int,values)]) 
    return grid

def calc_products(list):
    if len(list) < 4:
        return [] 
    products = [] 
    for i in range(len(list)-3):
        prod = 1 
        for j in range(4):
            prod *= list[i+j] 
        products.append(prod) 
    return products 

grid = np.array(load_grid()) 
products = [] 
# lines 
for line in grid:
    products += calc_products(line) 
# diagonals 
for line in [ grid.diagonal(i) for i in range(-19,20) ]: 
    products += calc_products(line) 

# columns 
grid2 = grid.transpose() 
for line in grid2:
    products += calc_products(line) 
# diagonals 
grid3 = grid[::-1,:] 
for line in [ grid3.diagonal(i) for i in range(-19,20) ]: 
    products += calc_products(line) 

print(max(products)) 
