actor_name = input()
academy_points = float(input())
jury = int(input())
flag = False

for n in range(jury):
    jury_name = input()
    jury_points = float(input())
    length_of_name = len(jury_name)

    current_points = (length_of_name * jury_points) / 2

    academy_points += current_points

    if academy_points >= 1250.5:
        flag = True
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break

if not flag:
    needed_score = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")