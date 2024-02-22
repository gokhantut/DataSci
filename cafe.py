# list
menu = ['chicken', 'coffee', 'hot drink', 'fruit']

# number of items
stock = {'chicken': 234, 'coffee': 678, 'hot drink': 57, 'fruit': 10}

# price of each item
price = {'chicken': 5, 'coffee': 4, 'hot drink': 6, 'fruit': 5}

# the total price od the stock
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# print the final total price
print(f"The total stock worth is : £{total_stock}")
