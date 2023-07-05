size = int(input())  # прочитаме размера на матрицата

matrix = []  # създаваме променлива, в която да пазим матрицата
bunny_pos = []  # създаваме променлива, в която да пазим позицията на заека
best_path = []  # създаваме променлива, в която да пазим най-добрия път

best_direction = None  # създаваме променлива, в която да пазим най-добрата посока
max_collected_eggs = 0  # създаваме променлива, в която да пазим максималния брой яйца

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]
    path = []
    collected_eggs = 0
    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)