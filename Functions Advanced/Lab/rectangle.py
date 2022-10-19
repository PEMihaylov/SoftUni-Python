# def rectangle(length, width):
#
#     def area(a, b):
#         rect_area = a * b
#         return rect_area
#
#     def perimeter(c, d):
#         perim_rect = 2*(c+d)
#         return perim_rect
#
#     if not isinstance(length, int) or not isinstance(width, int):
#         return "Enter valid values!"
#
#     return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


# print(rectangle(2, 10))


def rectangle(length, width):

    def area():
        rect_area = length * width
        return rect_area

    def perimeter():
        perim_rect = 2*(length+width)
        return perim_rect

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))