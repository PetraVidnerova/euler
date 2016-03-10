def foolDivide(x,y):
    del = [] 
    for x in str(x):
        for y in str(y):
            if x == y:
                del.append(x)
    for digit in del:
        x = int( str(x).replace(digit,"") )
        y = int( str(y).replace(digit,"") )
    return (x,y)

def isCurious(x,y):
    xs, ys = x, y 
    for i in range(99):
        if xs % i == 0 and ys % i == 0:
            xs = xs // i
            ys = ys // i
    if (xs,ys) == foolDivide(x,y):
        return True
    else:
        return False


for x in range(10,99):
    for y in range(10,99):
        if isCurious(x,y):
            print(x,y) 
