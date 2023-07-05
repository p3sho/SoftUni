total_days = int(input())
total_litres = 0
total_degrees = 0

for day in range(1,total_days + 1):
    litres = float(input())
    degrees = float(input())
    total_litres += litres
    total_degrees += litres * degrees

average_degrees = total_degrees / total_litres
print(f"Liter: {total_litres:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")