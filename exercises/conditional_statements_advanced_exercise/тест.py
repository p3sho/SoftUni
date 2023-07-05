month = input()
number_of_nights = int(input())

if month == 'May' or month == 'October':
        if 7 >= number_of_nights < 14:
            price_for_studio = (number_of_nights * 50) - ((number_of_nights * 50) * 0.05)
            print(f'Studio :{price_for_studio:.2f} lv.')
        elif number_of_nights >= 14:
            price_for_studio = (number_of_nights * 50) - ((number_of_nights * 50) * 0.30)
            price_apartment = (number_of_nights * 65) - ((number_of_nights * 65) * 0.10)
            print(f'Apartment: {price_apartment:.2f} lv.')
            print(f'Studio :{price_for_studio:.2f} lv.')

if month == 'June' or month == 'September':
    if number_of_nights <= 14:
        price_for_studio = 75.20 * number_of_nights
        price_apartment = 68.70 * number_of_nights
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio :{price_for_studio:.2f} lv.')
    elif number_of_nights > 14:
        price_for_studio = (75.20 - (75.20 * 0.20)) * number_of_nights
        price_apartment = (68.70 * number_of_nights) - ((68.70 * number_of_nights) * 0.10)
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio :{price_for_studio:.2f} lv.')