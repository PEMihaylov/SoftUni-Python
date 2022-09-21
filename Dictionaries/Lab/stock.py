inventory = input().split(' ')
inventory_products = {inventory[i]: int(inventory[i + 1]) for i in range(0, len(inventory), 2)}

# print(inventory_products)
products_to_search = input().split(' ')

for product in products_to_search:
    if product not in inventory_products:
        print(f"Sorry, we don\'t have {product}")
    else:
        print(f"We have {inventory_products[product]} of {product} left")





data = input().split()
search_data = input().split()


dictionary = {data[i]:data[i + 1] for i in range(0, len(data), 2)}

for element in search_data:
    if element in dictionary.keys():
        print(f"We have {dictionary[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")