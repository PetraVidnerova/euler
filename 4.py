def is_palindrom(number):
    s = str(number) 
    return s == s[::-1] 


palindroms = [] 
for i in range(111,1000):
    for j in range(111,1000):
        x = i*j 
        if is_palindrom(x):
            palindroms.append(x) 

print(max(palindroms)) 

