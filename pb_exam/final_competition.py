dancers = int(input())
points = float(input())
season = input()
place = input()

if place == 'Bulgaria':
    total_sum = dancers * points
    if season == 'winter':
        razhod = total_sum - (total_sum * 0.08)
        charity = razhod * 0.75
        print(f'Charity - {charity:.2f}')
        money_left = razhod - charity
        money_per_dancer = money_left / dancers
        print(f'Money per dancer - {money_per_dancer:.2f}')

    elif season == 'summer':
        razhod = total_sum - (total_sum * 0.05)
        charity = razhod * 0.75
        print(f'Charity - {charity:.2f}')
        money_left = razhod - charity
        money_per_dancer = money_left / dancers
        print(f'Money per dancer - {money_per_dancer:.2f}')

elif place == 'Abroad':
    total_sum = dancers * points + ((dancers * points) * 0.50)
    if season == 'winter':
        razhod = total_sum - (total_sum * 0.15)
        charity = razhod * 0.75
        print(f'Charity - {charity:.2f}')
        money_left = razhod - charity
        money_per_dancer = money_left / dancers
        print(f'Money per dancer - {money_per_dancer:.2f}')

    elif season == 'summer':
        razhod = total_sum - (total_sum * 0.10)
        charity = razhod * 0.75
        print(f'Charity - {charity:.2f}')
        money_left = razhod - charity
        money_per_dancer = money_left / dancers
        print(f'Money per dancer - {money_per_dancer:.2f}')