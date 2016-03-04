import re 

def name_score(name):
    total = 0 
    for x in name:
        total += ord(x)-ord('A')+1
    return total 

name_list = [] 
for name in open("p022_names.txt").read().split(","):
    name = re.findall("\"(.*)\"",name)[0] 
    name_list.append(name) 

name_list = sorted(name_list)

i=1
total = 0 
for name in name_list:    
    total += i*name_score(name) 
    i += 1 

print(total)
