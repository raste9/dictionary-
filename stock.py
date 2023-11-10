product_information = input().split()

stock_dictionary = {}

for i in range(0, len(product_information), 2):
    product = product_information[i]
    quantity = int(product_information[i + 1])
    stock_dictionary[product] = quantity

product_to_search = input().split()
for current_product in product_to_search:
    if current_product in stock_dictionary:
        print(f'We have {stock_dictionary[current_product]} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')

# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

# products = input().split()
# checking_products = input().split()
# dictionary = {}
#
# for i in range(0, len(products), 2):
#     product = products[i]
#     quantity = products[i + 1]
#     dictionary[product] = quantity
#
# for j in checking_products:
#     if j in dictionary.keys():
#         print(f'We have {dictionary[j]} of {j} left')
#     else:
#         print(f'Sorry, we don\'t have {j}')