def shopping_cart(*meals):
    cook_book = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for item in meals:
        if item == "Stop":
            break
        if item[0] == 'Soup' and len(cook_book['Soup']) < 3:
            if item[1] not in cook_book['Soup']:
                cook_book['Soup'].append(item[1])
        elif item[0] == 'Pizza' and len(cook_book['Pizza']) < 4:
            if item[1] not in cook_book['Pizza']:
                cook_book['Pizza'].append(item[1])
        elif item[0] == 'Dessert' and len(cook_book['Dessert']) < 2:
            if item[1] not in cook_book['Dessert']:
                cook_book['Dessert'].append(item[1])

    for product in cook_book.values():
        if len(product) > 0:
            break
    else:
        return "No products in the cart!"

    cook_book = sorted(cook_book.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for meal, product in cook_book:
        result.append(f"{meal}:")
        for prod in sorted(product):
            result.append(f" - {prod}")

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# #
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
# #

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
