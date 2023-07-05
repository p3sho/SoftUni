data = input()
users_data = {}

while data != ('Statistics'):
    current_command = input().split('=')

    if current_command[0] == 'Add':
        if current_command[1] not in users_data:
            users_data[current_command[1]] = int(current_command[2]) + int(current_command[3])

    elif current_command[0] == 'Message':
        if current_command[1] in users_data and current_command[2] in users_data:
            users_data[current_command[1]] += 1
            users_data[current_command[2]] += 1

    elif current_command[0] == 'Empty':
        if current_command[1] == 'All':
            users_data.clear()
        else:
            if current_command[1] in users_data:
                users_data.pop(current_command[1])
    else:
        break

print(f'Users count: {len(users_data)}')
for key, value in users_data.items():
    print(key, '-', value)
