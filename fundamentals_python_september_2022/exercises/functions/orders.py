product = input()
count = int(input())

if product == 'coffee':
    total_price = 1.5 * count
elif product == 'water':
    total_price = 1 * count
elif product == 'coke':
    total_price = 1.4 * count
elif product == 'snacks':
    total_price = 2 * count

print(f'{total_price:.2f}')