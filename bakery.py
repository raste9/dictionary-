products_quantity = input().split()

stock = {}

for i in range(0, len(products_quantity), 2):
    food = products_quantity[i]
    quantity = products_quantity[i + 1]
    stock[food] = int(quantity)

print(stock)

# input - bread 10 butter 4 sugar 9 jam 12
# output - {'bread': '10', 'butter': '4', 'sugar': '9', 'jam': '12'}
