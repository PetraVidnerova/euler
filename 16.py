import functools as func

print(func.reduce(lambda x,y: int(x)+int(y), str(2**1000)))

