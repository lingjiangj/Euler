# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

def CoinSums(money,coinlist):
    if len(coinlist) == 1:
        return 1
    sum = 0
    for i in range(len(coinlist)):
        if money - coinlist[i] == 0:
            sum += 1
        elif money - coinlist[i] > 0:
            sum += CoinSums(money-coinlist[i],coinlist[:i+1])
            
    return sum

print(CoinSums(200,[1,2,5,10,20,50,100,200]))
    
