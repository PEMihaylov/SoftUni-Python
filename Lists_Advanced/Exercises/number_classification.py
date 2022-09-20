# numbers_as_string = input().split(", ")
# numbers_as_digits = [int(number) for number in numbers_as_string]
# print(f"Positive: {', '.join(str(number) for number in numbers_as_digits if number >= 0)}")
# print(f"Negative: {', '.join(str(number) for number in numbers_as_digits if number < 0)}")
# print(f"Even: {', '.join(str(number) for number in numbers_as_digits if number % 2 == 0)}")
# print(f"Odd: {', '.join(str(number) for number in numbers_as_digits if number % 2 != 0)}")


# numbers_as_string = input().split(", ")
# print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")
# print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")
# print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")
# print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")


def positive_numbers(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


numbers_as_string = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers_as_string))}")
print(f"Positive: {', '.join(negative_numbers(numbers_as_string))}")
print(f"Positive: {', '.join(even_numbers(numbers_as_string))}")
print(f"Positive: {', '.join(odd_numbers(numbers_as_string))}")
