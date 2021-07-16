import collections
# create an empty variable for revenue
rev = 0
# Define amount of available shoes
number_of_shoes = int(input())
#Creates the variabl stock, which is a dictionary which holds the size and the amount of each size available.
stock = collections.Counter(map(int, input().split()))
#Number of customers
n = int(input())

for _ in range(n):
    #list that holds the size and the price of each size
    size, price = list(map(int, input().split()))
    #checks if the size is in stock
    if size in stock.keys():
        #checks that the size is available
        if stock[size] > 0:
            # adds the price of the size to the revenue
            rev += price
            # decreases 1 the amount of shoes of the size
            stock[size] -= 1

print(rev)


