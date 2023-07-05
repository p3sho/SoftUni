deposit = float(input())
months = int(input())
procent = float(input())

per_year = deposit * (procent / 100)
per_month = per_year / 12
total = deposit + (months * per_month)
print(total)