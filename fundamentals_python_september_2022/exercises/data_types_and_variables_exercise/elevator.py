from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())

courses = number_of_people // elevator_capacity
if courses * elevator_capacity < number_of_people:
    courses += 1
    print(courses)
else:
    print(courses)