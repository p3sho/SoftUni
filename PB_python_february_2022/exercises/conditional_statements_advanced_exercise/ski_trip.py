days = int(input())
room = input()
result = input()
nights = days - 1

if room == 'room for one person':
    price = nights * 18
    if result == 'positive':
        total_price = price + (price * 0.25)
    elif result == 'negative':
        total_price = price - (price * 0.10)
    print(f'{total_price:.2f}')

elif room == 'apartment':
    if nights < 10:
        price = (nights * 25) - ((nights * 25) * 0.30)
    elif 10 < nights < 15:
        price = (nights * 25) - ((nights * 25) * 0.35)
    elif nights > 15:
        price = (nights * 25) - ((nights * 25) * 0.50)
    if result == 'positive':
        total_price = price + (price * 0.25)
    elif result == 'negative':
        total_price = price - (price * 0.10)
    print(f'{total_price:.2f}')

elif room == 'president apartment':
    if nights < 10:
        price = (nights * 35) - ((nights * 35) * 0.10)
    elif 10 < nights < 15:
        price = (nights * 35) - ((nights * 35) * 0.15)
    elif nights > 15:
        price = (nights * 35) - ((nights * 35) * 0.20)
    if result == 'positive':
        total_price = price + (price * 0.25)
    elif result == 'negative':
        total_price = price - (price * 0.10)
    print(f'{total_price:.2f}')

