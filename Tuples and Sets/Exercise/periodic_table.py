N = int(input())

chemical_elements = set()

for _ in range(N):
    elements = input().split()
    for el in elements:
        chemical_elements.add(el)

print('\n'.join(chemical_elements))

# for el in chemical_elements:
#     print(elements)