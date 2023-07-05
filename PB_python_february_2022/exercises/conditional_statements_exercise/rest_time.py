from math import ceil
name_of_movie = input()
episode_duration = int(input())
duration_break = int(input())

time_to_lunch = duration_break * 1 / 8
time_to_break = duration_break * 1 / 4
time_left = duration_break - time_to_lunch - time_to_break

diff = ceil(abs(episode_duration - time_left))

if episode_duration <= time_left:
    print(f'You have enough time to watch {name_of_movie} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough aime to watch {name_of_movie}, you need {diff} more minutes.")