shop_list = input().split("!")
text = input()
while text != "Go Shopping!":
    data = text.split()
    command = data[0]
    product = data[1]
    if command == "Urgent":
        if product not in shop_list:
            shop_list.insert(0, product)
    elif command == "Unnecessary":
        if product in shop_list:
            shop_list.remove(product)
    elif command == "Correct":
        new_item = data[2]
        if product in shop_list:
            shop_list = [new_item if x == product else x for x in shop_list]
    elif command == "Rearrange":
        if product in shop_list:
            if product in shop_list:
                shop_list.remove(product)
                shop_list.insert(len(shop_list), product)

    text = input()

print(', '.join(shop_list))





#...neshto ne raboti


def urgent_func(product, shop_list):
    if product not in shop_list:
        return shop_list.insert(0, product)


def unnecessary_func(product, shop_list):
    if product in shop_list:
        return shop_list.remove(product)


def correct_func(product, new_item, shop_list):
    if product in shop_list:
        shop_list = [new_item if x == product else x for x in shop_list]
        return shop_list


def rearrange_func(product, shop_list):
    if product in shop_list:
        shop_list.remove(product)
        shop_list.insert(len(shop_list), product)
    return shop_list


shop_list = input().split("!")
text = input()
while text != "Go Shopping!":
    data = text.split()
    command = data[0]
    product = data[1]
    if command == "Urgent":
        urgent_func(product, shop_list)
    elif command == "Unnecessary":
        unnecessary_func(product, shop_list)
    elif command == "Correct":
        new_item = data[2]
        correct_func(product, new_item, shop_list)
    elif command == "Rearrange":
        rearrange_func(product, shop_list)

    text = input()

print(', '.join(shop_list))



