rows, columns = tuple(map(int, input().split()))
snake = input()
idx = 0
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(snake[idx % len(snake)])
        idx += 1

    if row % 2 == 0:
       print(''.join(map(str, matrix[row])))

    else:
       print(''.join(map(str, matrix[row][::-1])))


