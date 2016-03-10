def foolDivide(x,y):
    todel = [] 
    for xs in str(x):
        for ys in str(y):
            if xs == ys:
                todel.append(xs)
    for digit in todel:
        xs = str(x).replace(digit,"") 
        ys =  str(y).replace(digit,"")
        if xs == "":
            x = 1
        else:
            x = int(xs)
        if ys == "":
            y = 1
        else:
            y = int(ys)
    if y == 0:
        return (x,y,False)
    return (x,y,bool(todel))

def divide(x,y):
    for i in range(x+1,1,-1):
        if x % i == 0 and y % i == 0:
            x = x // i
            y = y // i
    return (x,y) 

def isCurious(x,y):
    if x == y:
        return False
    if x / y >= 1:
        return False
        
    if x % 10 == 0 and y % 10 == 0:
        return False

    (x1, y1) = divide(x,y)
    (x2, y2, divided) = foolDivide(x,y)
    if not divided:
        return False
    else:
        return x1/y1 == x2/y2 

curious_tuples = []         
for x in range(10,99):
    for y in range(10,99):
        if isCurious(x,y):
            curious_tuples.append((x,y))


print(curious_tuples)

x, y = 1, 1
for (a, b) in curious_tuples:
    x *= a
    y *= b

print(x, y)
print(divide(x,y))
