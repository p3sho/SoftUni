from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())
bonuses = []
student_attendances = []

for i in range(1, students + 1):
    student_attendance = int(input())
    bonuses.append(ceil(student_attendance / lectures * (5 + additional_bonus)))
    student_attendances.append(student_attendance)

print(f'Max Bonus: {max(bonuses)}.')
print(f'The student has attended {max(student_attendances)} lectures.')