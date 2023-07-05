from collections import deque


def is_valid_position(position, rows, cols):
    row, col = position
    return 0 <= row < rows and 0 <= col < cols


def find_mouse_position(matrix, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'M':
                return (row, col)


def all_cheese_eaten(matrix):
    for row in matrix:
        if 'C' in row:
            return False
    return True


def update_matrix(matrix, mouse_position):
    row, col = mouse_position
    matrix[row][col] = '*'


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def simulate_mouse_movement(matrix, rows, cols):
    mouse_position = find_mouse_position(matrix, rows, cols)
    directions = deque()
    trapped = False
    cheese_eaten = False

    while True:
        direction = input()
        if direction == 'danger':
            break
        directions.append(direction)

    while directions:
        direction = directions.popleft()
        row, col = mouse_position

        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            col -= 1
        elif direction == 'right':
            col += 1

        if is_valid_position((row, col), rows, cols):
            if matrix[row][col] == '@':
                continue
            elif matrix[row][col] == 'C':
                matrix[row][col] = '*'
                update_matrix(matrix, mouse_position)
                mouse_position = (row, col)
                if all_cheese_eaten(matrix):
                    matrix[row][col] = "M"
                    cheese_eaten = True
                    break
            elif matrix[row][col] == 'T':
                update_matrix(matrix, mouse_position)
                mouse_position = (row, col)
                matrix[row][col] = 'M'
                trapped = True
                break
            elif matrix[row][col] == '*':
                update_matrix(matrix, mouse_position)
                mouse_position = (row, col)
        else:
            print('No more cheese for tonight!')
            matrix[mouse_position[0]][mouse_position[1]] = 'M'
            print_matrix(matrix)
            return

    if cheese_eaten:
        print('Happy mouse! All the cheese is eaten, good night!')
    elif trapped:
        print('Mouse is trapped!')
    else:
        print('Mouse will come back later!')

    print_matrix(matrix)


rows, cols = map(int, input().split(','))
matrix = []
for _ in range(rows):
    row = list(input())
    matrix.append(row)

simulate_mouse_movement(matrix, rows, cols)