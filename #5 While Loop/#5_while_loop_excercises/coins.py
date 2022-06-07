resto = float(input())
dimes = round(resto * 100)
coins = 0

while dimes > 0:
    if dimes >= 200:
        coins += 1
        dimes = dimes - 200
    elif dimes >= 100:
        coins += 1
        dimes = dimes - 100
    elif dimes >= 50:
        coins += 1
        dimes = dimes - 50
    elif dimes >= 20:
        coins += 1
        dimes = dimes - 20
    elif dimes >= 10:
        coins += 1
        dimes = dimes - 10
    elif dimes >= 5:
        coins += 1
        dimes = dimes - 5
    elif dimes >= 2:
        coins += 1
        dimes = dimes - 2
    elif dimes >= 1:
        coins += 1
        dimes = dimes - 1


print(coins)
