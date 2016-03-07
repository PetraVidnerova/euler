import itertools
coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ] 

def num_of_ways(count):
    ways = 0
    for coin in coins:
        if coin < count:
            ways += num_of_ways(count-coin)
        if coin == count:
            ways += 1
            continue 
    return ways
            

print(num_of_ways(200))
