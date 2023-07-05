students = int(input())
top_students = 0
average_students = 0
lower_students = 0
fail = 0
average = 0

for student in range(1, students + 1):
    grade = float(input())
    average += grade
    if grade >= 5:
        top_students += 1
    elif 4 <= grade <= 4.99:
        average_students += 1
    elif 3 <= grade <= 3.99:
        lower_students += 1
    elif grade < 3:
        fail += 1

print(f'Top students: {top_students / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {average_students / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {lower_students / students * 100:.2f}%')
print(f'Fail: {fail / students * 100:.2f}%')
print(f'Average: {average / students:.2f}')