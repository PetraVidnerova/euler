coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ] 

def list2str(x):
    res = str(x[0]) 
    for i in range(1,len(x)):
        res += ","+str(x[i])
    return res 


def str2list(x):
    return [x for x in map(int,x.split(","))] 


ways = [set(),set()]
ways[0].add(list2str([0,0,0,0,0,0,0,0]))
ways[1].add(list2str([1,0,0,0,0,0,0,0]))
 

for i in range(2,201):
    print(i)
    ways_i = set()
    for coin in range(0,8):
        if i-coins[coin] >= 0:
            for combination in ways[i-coins[coin]]:
                newcomb = str2list(combination) 
                newcomb[coin]=newcomb[coin]+1
                newcomb = list2str(newcomb) 
                if newcomb not in ways_i:
                    ways_i.add(newcomb); 
    ways.append(ways_i)


print(len(ways[200]))

