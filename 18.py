triangle = [] 
for line in open("input18.txt"):
    triangle.append([x for x in map(int, line.split())])

print(triangle)
