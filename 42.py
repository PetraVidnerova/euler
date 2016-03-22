import math

def isTriangle(x):
    for n in range(1,x+1):
        if 2*x/n == n+1:
            return True 
    return False

def getCount(word):
    ret = 0
    for c in word:
        ret += ord(c)-ord('A')+1
    return ret 


count = 0        
for word in open("p042_words.txt").read().split(","):
    word = word.strip("\"")
    word_count = getCount(word)
    if isTriangle(word_count):
        count += 1

print(count)
