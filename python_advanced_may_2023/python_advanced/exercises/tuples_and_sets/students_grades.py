n = int(input())

students_grades = {}

for _ in range(n):
    name, grade = tuple(input().split())
    grade = float(grade)
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for name, grade in students_grades.items():
    avg = sum(grade) / len(grade)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grade])} (avg: {avg:.2f})")