pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())
total_hours = pages // pages_per_hour
hours_per_day = total_hours // days_to_read
print(hours_per_day)
