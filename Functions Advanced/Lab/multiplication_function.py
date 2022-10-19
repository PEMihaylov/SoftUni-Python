def multiply(*args):
    res = 1
    for n in args:
        res *= n
    return(res)

print(multiply(2, 0, 1000, 5000))

