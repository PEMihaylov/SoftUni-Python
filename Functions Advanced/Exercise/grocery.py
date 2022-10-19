def grocery_store(**prd_qty):
    result = ''
    prd_qty = dict(sorted(prd_qty.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for key, value in prd_qty.items():
        result += f"{key}: {value}" + '\n'
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggsf=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
