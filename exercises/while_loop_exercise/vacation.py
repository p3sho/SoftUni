vac_price = int(input())
available_money = int(input())
day_counter = 0
spednind_counter = 0
flag = False

while available_money <= vac_price:
    command = input()
    current_sum = int(input())
    day_counter += 1

    if command == 'spend':
        spednind_counter += 1
        if spednind_counter == 5:
            print(f"You can't save the money.")
            print(f'{day_counter}')
            flag = True
            break

        if current_sum > available_money:
            available_money = 0
        else:
            available_money -= current_sum

    elif command == 'save':
        spednind_counter = 0
        available_money += current_sum

if not flag:
    print(f'You saved the money for {day_counter} days.')
