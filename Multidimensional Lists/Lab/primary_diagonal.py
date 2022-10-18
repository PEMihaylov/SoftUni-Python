N = int(input())

matrix = [[int(x) for x in input().split()] for i in range(N)]

diagonal_sum = 0

for i in range(N):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)