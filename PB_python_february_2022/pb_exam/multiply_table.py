text_num = input()
reversed_text = text_num[::-1]
list_nums = list(reversed_text)

for x in range(1, int(list_nums[0]) + 1):
    for y in range(1, int(list_nums[1]) + 1):
        for z in range(1, int(list_nums[2]) + 1):
            sum_of_nums = x * y * z
            print(f"{x} * {y} * {z} = {sum_of_nums};")