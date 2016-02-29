x = 1
y = 1 
x_even =  False
y_even =  False 
sum = 0 

while y <= 4000000:
    new = x + y
    # both true is not possible 
    if (not x_even) and (not y_even):
        new_even = True
        sum += new 
    else:
        new_even = False 

    x = y
    y = new 
    x_even = y_even
    y_even = new_even
    

print(sum)
