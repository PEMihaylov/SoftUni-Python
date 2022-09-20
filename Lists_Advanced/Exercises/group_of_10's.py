string = input().split(", ")
digits = list(map(int, string))

max_num = max(digits)
boundary = 10
for num in digits:
    filtered = filter(lambda nums: nums <= boundary, digits)
    delta = list(filtered)
    print(f"Group of {boundary}'s: {delta}")
    for i in delta:
        digits.remove(i)
    boundary += 10

