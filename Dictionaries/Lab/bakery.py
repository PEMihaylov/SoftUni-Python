data = input().split(' ')
products_dict = {}

# for i in range(0, len(data), 2):
#     products_dict[data[i]] = int(data[i + 1])

# dict comprehension
products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

print(products_dict)



text = input().split(" ")

bakery = {}
for element in range(0, len(text), 2):
    key = text[element]
    value = text[element +1]
    bakery[key] = int(value)
print(bakery)