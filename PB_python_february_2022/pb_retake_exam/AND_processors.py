import math

processors = int(input())
workers = int(input())
working_days = int(input())

all_hours = 8 * workers * working_days
maked_processors = math.floor(all_hours / 3)

processors_diff = processors - maked_processors
money_losse = processors_diff * 110.10

diff = (maked_processors - processors) * 110.10

if maked_processors < processors:
    print(f'Losses: -> {money_losse:.2f} BGN')
elif maked_processors >= processors:
    print(f'Profit: -> {diff:.2f} BGN')