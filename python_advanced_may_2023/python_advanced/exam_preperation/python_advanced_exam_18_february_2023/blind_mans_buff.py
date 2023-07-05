def play_blind_mans_buff(N, M, playground):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'right': (0, 1),
        'left': (0, -1)
    }
    row, col = find_starting_position(playground)
    touched_opponents = 0
    moves_made = 0

    while True:
        command = input().strip()
        if command == 'Finish':
            break

        if command not in directions:
            continue

        d_row, d_col = directions[command]
        new_row, new_col = row + d_row, col + d_col

        if not is_valid_position(new_row, new_col, N, M):
            continue

        if playground[new_row][new_col] == 'O':
            continue

        if playground[new_row][new_col] == 'P':
            touched_opponents += 1
            playground[new_row][new_col] = '-'

        row, col = new_row, new_col
        moves_made += 1

    print("Game over!")
    print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


def find_starting_position(playground):
    for i in range(len(playground)):
        for j in range(len(playground[i])):
            if playground[i][j] == 'B':
                return i, j


def is_valid_position(row, col, N, M):
    return 0 <= row < N and 0 <= col < M


# Read the dimensions of the playground
N, M = map(int, input().split())

# Read the playground rows
playground = []
for _ in range(N):
    row = input().split()
    playground.append(row)

# Start the game
play_blind_mans_buff(N, M, playground)
