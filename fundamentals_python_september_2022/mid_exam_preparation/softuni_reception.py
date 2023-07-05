from math import ceil

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
hours = 0

students_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
students_left = students_count - students_per_hour
maked_students = ceil(students_count / students_per_hour)
while students_left < students_per_hour:
    hours += 1

print(f'Time needed: {maked_students + hours}h.')

#puuuuu