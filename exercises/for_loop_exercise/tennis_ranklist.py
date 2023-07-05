number_of_torunaments = int(input())
starting_points = int(input())

points = 0
number_of_winning = 0

for _ in range(number_of_torunaments):
    stage_of_tournamet = input()

    if stage_of_tournamet == 'SF':
        points += 720
    elif stage_of_tournamet == 'F':
        points += 1200
    elif stage_of_tournamet == 'W':
        points += 2000
        number_of_winning += 1

average_points = points / number_of_torunaments
total_points = starting_points + points
print(f'Final points: {total_points}')
print(f'Average points: {int(average_points)}')
print(f'{number_of_winning / number_of_torunaments * 100:.2f}%')