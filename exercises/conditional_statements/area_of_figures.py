from math import pi

figure = str(input())

if figure == 'square':
    square_side = float(input())
    square_area = square_side * square_side
    print("{0:.3f}".format(square_area))

elif figure == 'rectangle':
    rectangle_side1 = float(input())
    rectangle_side2 = float(input())
    rectangle_area = rectangle_side1 * rectangle_side2
    print("{0:.3f}".format(rectangle_area))

elif figure == 'circle':
    circle_radius = float(input())
    circle_area = pi * circle_radius ** 2
    print("{0:.3f}".format(circle_area))

elif figure == 'triangle':
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = (triangle_side * triangle_height) / 2
    print("{0:.3f}".format(triangle_area))