from math import floor


def distance_to_center(x, y):
    return (x ** 2 + y ** 2) ** 0.5


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    """calculate the distance between the two points"""
    distance1 = distance_to_center(x1, y1)
    distance2 = distance_to_center(x2, y2)
    distance3 = distance_to_center(x3, y3)
    distance4 = distance_to_center(x4, y4)
    line_one = distance1 + distance2
    line_two = distance3 + distance4

    '''Check which line is longer'''
    if line_one >= line_two:
        p1 = (x1, y1) if distance1 <= distance2 else (x2, y2)
        p2 = (x2, y2) if distance1 <= distance2 else (x1, y1)
    else:
        p1 = (x3, y3) if distance3 <= distance4 else (x4, y4)
        p2 = (x4, y4) if distance3 <= distance4 else (x3, y3)

    return f'({floor(p1[0])}, {floor(p1[1])})({floor(p2[0])}, {floor(p2[1])})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)

print(result)

# from math import floor
# 
#
# def distance_to_center(x, y):
#     return (x ** 2 + y ** 2) ** 0.5
#
#
# def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
#     """calculate the distance between the two points"""
#     distance1 = distance_to_center(x1, y1) + distance_to_center(x2, y2)
#     distance2 = distance_to_center(x3, y3) + distance_to_center(x4, y4)
#
#     '''Check which line is longer'''
#     if distance1 >= distance2:
#         if distance_to_center(x1, y1) <= distance_to_center(x2, y2):
#             return f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})'
#         else:
#             return f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})'
#     else:
#         if distance_to_center(x3, y3) <= distance_to_center(x4, y4):
#             return f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})'
#         else:
#             return f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})'
#
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x3 = float(input())
# y3 = float(input())
# x4 = float(input())
# y4 = float(input())
# result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
#
# print(result)