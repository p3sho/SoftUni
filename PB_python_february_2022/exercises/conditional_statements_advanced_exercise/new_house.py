type_flowers = input()
flowers_count = int(input())
budget = int(input())
costs = 0

if type_flowers == 'Roses':
    costs = 5 * flowers_count
    if flowers_count > 80:
        costs -= costs * 0.10
elif type_flowers == 'Dahlias':
    costs = 3.80 * flowers_count
    if flowers_count > 90:
        costs -= costs * 0.15
elif type_flowers == 'Tulips':
    costs = 2.80 * flowers_count
    if flowers_count > 80:
        costs -= costs * 0.15
elif type_flowers == 'Narcissus':
    costs = 3 * flowers_count
    if flowers_count < 120:
        costs += costs * 0.15
elif type_flowers == 'Gladiolus':
    costs = 2.50 * flowers_count
    if flowers_count < 80:
        costs += costs * 0.20

diff = abs(budget - costs)
if budget >= costs:
    print(f"Hey, you have a great garden with {flowers_count} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")