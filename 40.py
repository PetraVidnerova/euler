num_string="."
i=1
while len(num_string)<1000001:
    num_string += str(i)
    i += 1 

prod = 1 
for d in [10, 100, 1000, 10000, 100000, 1000000]:  
    prod *= int(num_string[d]) 

print(prod)
