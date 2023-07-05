from person import Person
from employee import Employee
from teacher import Teacher

# Create an instance of Person
person = Person()
print(person.sleep())  # Output: sleeping...

# Create an instance of Employee
employee = Employee()
print(employee.get_fired())  # Output: fired...

# Create an instance of Teacher
teacher = Teacher()
print(teacher.sleep())  # Output: sleeping...
print(teacher.get_fired())  # Output: fired...
print(teacher.teach())  # Output: teaching...
