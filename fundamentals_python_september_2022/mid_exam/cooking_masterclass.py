from math import ceil

budget = float(input())
students = int(input())
package_flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())
free_packages_flour = 0

for student in range(1, students +1):
    if student % 5 == 0:
        free_packages_flour += 1

total_money = (single_apron_price * (ceil(students * 1.2))) + (single_egg_price * 10 * students) + (package_flour_price * (students - free_packages_flour))

if budget >= total_money:
    print(f"Items purchased for {total_money:.2f}$.")
else:
    difference = total_money - budget
    print(f"{difference:.2f}$ more needed.")