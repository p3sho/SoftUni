hour_exam = int(input())
minute_exam = int(input())
come_hour = int(input())
come_minutes = int(input())

time_for_exam = hour_exam * 60 + minute_exam
time_for_arrival = come_hour * 60 + come_minutes
diff = abs(time_for_exam - time_for_arrival)

if time_for_exam == time_for_arrival:
    print('On time')

elif time_for_arrival > time_for_exam:
    print('Late')
    hours = diff // 60
    minutes = diff % 60

    if diff > 59:
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')

elif time_for_arrival < time_for_exam:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    else:
        print('Early')
        hours = diff // 60
        minutes = diff % 60

        if diff > 59:
            print(f'{hours}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')