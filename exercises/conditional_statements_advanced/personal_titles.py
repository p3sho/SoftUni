age = float(input())
gender = input()

if gender == 'm' and age >= 16:
    print(f'Mr.')
elif gender == 'm' and age < 16:
    print(f'Master')
elif gender == 'f' and age >= 16:
    print(f'Ms.')
elif gender == 'f' and age < 16:
    print(f'Miss')