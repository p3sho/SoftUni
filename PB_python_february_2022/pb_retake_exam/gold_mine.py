location = int(input())

for _ in range(1, location + 1):
    expected_avarage = int(input())
    number_of_days_ped_location = int(input())
    gold_location_sum = 0
    for nesh in range(1, number_of_days_ped_location +1):
        gold_gained_for_the_day = int(input())

        gold_location_sum += gold_gained_for_the_day
    actual_average = gold_location_sum / number_of_days_ped_location

    if actual_average >= expected_avarage:
        print(f'Good job! Average gold per day: {actual_average:.2f}.')
    elif actual_average < expected_avarage:
        diff = abs(expected_avarage - actual_average)
        print(f'You need {diff:.2f} gold.')
