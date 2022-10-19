def negative_numbers(nums):
    neg_sum = 0
    for n in nums:
        if int(n) < 0:
            neg_sum += n
    return neg_sum


def positive_numbers(nums):
    pos_sum = 0
    for n in nums:
        if int(n) > 0:
            pos_sum += n
    return pos_sum


numbers = tuple(map(int, input().split()))
# numbers = [int(i) for i in input().split()]

print(negative_numbers(numbers))
print(positive_numbers(numbers))
if abs(negative_numbers(numbers)) > positive_numbers(numbers):
    print("The negatives are stronger than the positives")
elif abs(negative_numbers(numbers)) < positive_numbers(numbers):
    print("The positives are stronger than the negatives")


