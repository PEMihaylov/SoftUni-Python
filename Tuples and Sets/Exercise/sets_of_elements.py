N, M = input().split()
first_set = set()
second_set = set()

for _ in range(int(N)):
    first_set.add(input())

for ele in range(int(M)):
    second_set.add(input())

res = first_set & second_set
print('\n'.join(res))


#..........

# N, M = map(int, tuple(input().split()))
# first_set, second_set = set(), set()
