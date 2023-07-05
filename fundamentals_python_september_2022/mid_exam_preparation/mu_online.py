rooms = [data.split() for data in input().split("|")]

health = 100
bitcoins = 0
alived_rooms = 0

for room in rooms:
    item, value = [int(x) if x.isdigit() else x for x in room]
    alived_rooms += 1

    if item == 'potion':
        if health + value >100:
            value = 100 - health
        health += value
        print(f'You healed for {value} hp.')
        print(f'Current health: {health} hp.')

    elif item == 'chest':
        bitcoins += value
        print(f'You found {value} bitcoins.')

    else:
        if health - value <= 0:
            print(f"You died! Killed by {item}.")
            print(f"Best room: {alived_rooms}")
            break
        else:
            health -= value
            print(f'You slayed {item}.')
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
