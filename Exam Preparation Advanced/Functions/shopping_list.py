def shopping_list(budget, **kwargs):
    shop_list = {}

    if budget >= 100:
        for key, value in kwargs.items():
            price = float(value[0]) * int(value[1])
            if len(shop_list) < 5:
                if price <= budget:
                    shop_list[key] = price
                    budget -= price

        result = []
        for k, v in shop_list.items():
            result.append(f"You bought {k} for {v:.2f} leva.")

        return '\n'.join(result)

    else:
        return "You do not have enough budget."


# #
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# # #
# # print(shopping_list(20,
# #                     jeans=(19.99, 1),
# #                     ))
# # #
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
