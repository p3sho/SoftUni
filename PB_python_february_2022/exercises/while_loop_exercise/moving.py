width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())

availeble_free_space = width_of_free_space * length_of_free_space * height_of_free_space
occupied_place = 0

while True:
    command = input()

    if command == 'Done':
        break

    occupied_place += int(command)

    if occupied_place > availeble_free_space:
        break
diff = abs(occupied_place - availeble_free_space)

if availeble_free_space >= occupied_place:
    print(f'{diff} Cubic meters left.')
else:
    print(f'No more free space! You need {diff} Cubic meters more.')