from math import floor


def closest_to_the_center(x1, y1, x2, y2):
    """calculate the distance from the center (0,0)"""
    distance1 = ((x1 - 0) ** 2 + (y1 - 0) ** 2) ** 0.5
    distance2 = ((x2 - 0) ** 2 + (y2 - 0) ** 2) ** 0.5
    if distance1 <= distance2:
        return f'({floor(x1)}, {floor(y1)})'
    else:
        return f'({floor(x2)}, {floor(y2)})'


coordinate_x1 = float(input())
coordinate_y1 = float(input())
coordinate_x2 = float(input())
coordinate_y2 = float(input())
result = closest_to_the_center(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2)

print(result)
