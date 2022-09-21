squares = {1: 'one', 2: "two", 3: "three"}
squares_1 = {5: 'five'}
# for el in squares.keys():
#     print(el)
#
# for el in squares.items():
#     print(el)
#
# for el in squares.values():
#     print(el)
#
# for key, value in squares.items():
#     print(key, value)
#
# for value in squares.values():
#     print(value, end = " ")
#
# for key in squares.keys():
#     print(squares[key], end=" ")

squares.update(squares_1)
print(squares)

squares_1[5] += ', example'
print(squares_1)
# squares.setdefault(4, "four")
# print(squares)


# print(squares.get(1))

# del squares[1]
# print(squares)

# print(squares.popitem())
#
# squares.copy()
# print(squares)
#
# squares.pop(1)
# print(squares)
#
#
# squares.clear()
# print(squares)

dict