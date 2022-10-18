N = int(input())

unique_users = set()

for _ in range(N):
    unique_users.add(input())

print('\n'.join(unique_users))

