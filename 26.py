def len_rec_cycle(d): 
    num = 1 
    digits = []
    repository = []  
    while num > 0:
        num *= 10
        digit = num // d 
        num = num % d
        # if starting cycle break
        if (digit,num) in repository:
            break
        digits.append(digit)
        repository.append((digit,num))
    if num == 0:
        return 0
    else:
        # The len of recurring cycle is 
        # the len of the part of repository
        # after (digit, num). 
        len = 0
        for x, y in repository:
            if (x, y) == (digit, num):
                len = 1
                continue
            if len > 0:
                len += 1
        return len
        
max = None
maxd = None
for i in range(1,1000):
    len = len_rec_cycle(i)
    if max == None or max < len:
        max = len
        maxd = i 

print(maxd, max)
