import itertools 
digits = [ x for x in range(10) ] 

i = 0
for x in itertools.permutations(digits):
    i += 1
    if i == 1000000:
        print(x)
        break 

for c in x:
    print(c,end="")


