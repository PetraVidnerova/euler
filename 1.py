multiples = [] 
x = 3 
while x < 1000:
    multiples.append(x)
    x += 3 

x = 5 
while x < 1000:
    if x not in multiples:
        multiples.append(x) 
    x += 5 

print(sum(multiples))
