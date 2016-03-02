numbers = [] 
for line in open("input13.txt"):
    numbers.append(line.strip())

result = ""
rest = 0 
for i in range(49,-1,-1):
    # make sum of rest and digits on ith position
    sum = rest 
    for line in numbers:
        sum += int(line[i])
    # split the curent digit and the rest 
    digit = sum % 10 
    rest = sum // 10 
    result = str(digit)+result 
result = str(rest)+result 
print(result[:10])
