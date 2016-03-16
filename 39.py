def sidesforperimeter(p):
    sides = []  
    for a in range(1,p):
        for b in range(1,p):
            c = p - a - b
            if a*a + b*b == c*c:
                sides.append((a,b,c))
    return sides

max = None
max_p = None
for p in range(1,1001):
    print(p)
    c = len(sidesforperimeter(p))
    if max == None or c > max:
        max = c
        max_p = p

print(max_p)
