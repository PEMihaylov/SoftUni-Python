N = int(input())
odd_set, even_set = set(), set()

for row in range(1, N+1):
    name = input()
    name_ascii = 0
    for i in name:
        name_ascii += ord(i)
    name_ascii /= row
    if name_ascii % 2 == 0:
        even_set.add(name_ascii)
    else:
        odd_set.add(name_ascii)

if sum(odd_set) == sum(even_set):
    print(', '.join(map(str, odd_set.union(even_set))))
elif sum(odd_set) > sum(even_set):
    print(', '.join(map(str, odd_set.difference(even_set))))
elif sum(odd_set) < sum(even_set):
    print(', '.join(map(str, odd_set.symmetric_difference(even_set))))

