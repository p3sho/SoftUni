world_record = float(input())
distance = float(input())
time_in_sec_for_meter = float(input())

distance_all = distance * time_in_sec_for_meter
add_time = (distance // 15) * 12.5

total_time = distance_all + add_time

missing_time = 0

if world_record <= total_time:
    missing_time = abs(total_time - world_record)
    print(f"No, he failed! He was {missing_time:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
