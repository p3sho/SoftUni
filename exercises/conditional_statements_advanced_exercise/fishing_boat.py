budget = int(input())
season = input()
fishers = int(input())
price = 0

if season == 'Spring':
    if fishers <= 6:
        price = 3000 - (3000 * 0.1)
    elif 7 < fishers <= 11:
        price = 3000 - (3000 * 0.15)
    elif fishers >= 12:
        price = 3000 - (3000 * 0.25)
    if fishers % 2 == 0:
        price -= price * 0.05

elif season == 'Summer':
    if fishers <= 6:
        price = 4200 - (4200 * 0.1)
    elif 7 < fishers <= 11:
        price = 4200 - (4200 * 0.15)
    elif fishers >= 12:
        price = 4200 - (4200 * 0.25)
    if fishers % 2 == 0:
        price -= price * 0.05

elif season == 'Autumn':
    if fishers <= 6:
        price = 4200 - (4200 * 0.1)
    elif 7 < fishers <= 11:
        price = 4200 - (4200 * 0.15)
    elif fishers >= 12:
        price = 4200 - (4200 * 0.25)

elif season == 'Winter':
    if fishers <= 6:
        price = 2600 - (2600 * 0.1)
    elif 7 < fishers <= 11:
        price = 2600 - (2600 * 0.15)
    elif fishers >= 12:
        price = 2600 - (2600 * 0.25)
    if fishers % 2 == 0:
        price -= price * 0.05

diff = abs(budget - price)

if budget < price:
    print(f"Not enough money! You need {diff:.2f} leva.")
elif budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")