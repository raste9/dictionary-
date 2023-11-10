stock = {}

while True:
    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(": ")
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

product_count = len(stock)
total_quantity = sum(stock.values())

print('Products in stock:')

for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_quantity}')

# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics

# dictionary = {}
#
# while True:
#     line = input()
#     if line == 'statistics':
#         break
#     product, quantity = line.split(": ")
#
#     if product not in dictionary.keys():
#         dictionary[product] = int(quantity)
#     else:
#         dictionary[product] += int(quantity)
#
# print(f'Products in stock:')
#
# [print(f'- {key}: {value}') for key, value in dictionary.items()]
#
# print(f'Total Products: {len(dictionary.keys())}')
# print(f'Total Quantity: {sum(dictionary.values())}')










