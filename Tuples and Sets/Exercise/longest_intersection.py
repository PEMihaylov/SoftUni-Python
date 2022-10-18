N = int(input())

final_list = {}

for i in range(N):
    range_1, range_2 = input().split("-")
    first_limit_1, second_limit_1 = tuple(map(int, range_1.split(",")))
    first_limit_2, second_limit_2 = tuple(map(int, range_2.split(",")))
    a_set = {num for num in range(first_limit_1, second_limit_1 + 1)}
    b_set = {num for num in range(first_limit_2, second_limit_2 + 1)}
    intersection = a_set.intersection(b_set)

    if len(intersection) > len(final_list):
        final_list = intersection

print(f"Longest intersection is [{', '.join(map(str, {i for i in final_list}))}] with length {len(final_list)}")

