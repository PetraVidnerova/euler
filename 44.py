pentagonal = set() 
pentagonal2 = [] 
couples = [] 

for i in range(1,10000):
    x = i*(3*i-1)/2 
    pentagonal.add(x) 
    pentagonal2.append(x) 

for x in pentagonal2:
    for y in pentagonal2:
        if x == y: continue
        if x+y in pentagonal and abs(x-y) in pentagonal: 
            couples.append((x,y))

print(couples)
min = None
for x,y in couples:
    if min == None or abs(x-y) < min:
        min = abs(x-y)

print(min)
