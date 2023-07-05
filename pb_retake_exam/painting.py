import math

paint_count = int(input())
rolls_count = int(input())
gloves_price = float(input())
brush_price = float(input())

price_paint = paint_count * 21.50
price_roll_paper = rolls_count * 5.20
gloves_needed = math.ceil(rolls_count * 0.35)
brush_needed = math.floor(paint_count * 0.48)

gloves = gloves_price * gloves_needed
brush = brush_price * brush_needed

total_price = price_paint + price_roll_paper + gloves + brush

delivery_price = total_price / 15
print(f'This delivery will cost {delivery_price:.2f} lv.')