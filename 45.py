triangle = set() 
for i in range(1,100000):
    triangle.add( i*(i+1)//2 )

pentagonal = set() 
for i in range(1,100000):
    pentagonal.add( i*(3*i-1) // 2)

for i in range(1,100000):
    hexagonal = i*(2*i-1)
    if hexagonal in triangle and hexagonal in pentagonal:
        print(hexagonal)
