import functools as func

numbers = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", ] 

tens = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eigthy", "ninety" ] 

for x in tens:
    numbers.append(x) 
    for y in numbers[:9]:
        numbers.append(x+y)

for x in numbers[:9]:
    numbers.append(x+"hundred") 
    for y in numbers[:99]:
        numbers.append(x+"hundredand"+y)
numbers.append("onethousand")

print(numbers)

print(len(func.reduce(lambda x,y: x+y, numbers)))
