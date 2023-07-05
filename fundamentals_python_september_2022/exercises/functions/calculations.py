operation = input()
first_num = int(input())
second_num = int(input())
result = None

if operation == 'multiply':
    result = first_num * second_num
elif operation == 'divide':
    result = first_num // second_num
elif operation == 'add':
    result = first_num + second_num
elif operation == 'subtract':
    result = first_num - second_num

print(result)
