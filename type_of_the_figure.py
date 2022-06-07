from math import pi

type_of_the_figure = input()
result = 0
if type_of_the_figure == "square":
    side = float(input())
    result = side * side
elif type_of_the_figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    result = side2 * side1
elif type_of_the_figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif type_of_the_figure == "triangle":  #else
    side = float(input())
    height = float(input())
    result = (side * height) / 2

print(result)