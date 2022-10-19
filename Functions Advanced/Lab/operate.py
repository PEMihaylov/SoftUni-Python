from functools import reduce


def operate(operator, *numbers):

    if operator == "+":
        result = reduce(lambda x, y: x + y, numbers)

    elif operator == "-":
        result = reduce(lambda x, y: x - y, numbers)

    elif operator == "*":
        result = reduce(lambda x, y: x * y, numbers)

    elif operator == "/":
        result = reduce(lambda x, y: x / y, numbers)

    return result


print(operate("+", 1, 2, 3))