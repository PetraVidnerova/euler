def next_fib(f1,f2):
    return f1+f2 

def digits(x):
    return len(str(x)) 

f1 = 1
f2 = 1
i = 2 
while digits(f2)<1000:
    x = next_fib(f1, f2)
    f1 = f2 
    f2 = x 
    i += 1 

print(i)
