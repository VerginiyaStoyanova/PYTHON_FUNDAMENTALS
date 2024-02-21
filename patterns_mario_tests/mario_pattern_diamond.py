# number = int(input())
#
# if number % 2 == 0:
#     number += 1
#
# for i in range(1, number + 1, 2):
#     spaces = " " * ((number - i) // 2)
#     stars = "*" * i
#     print(spaces + stars)
#
# for i in range(number - 2, 0, -2):
#     spaces = " " * ((number - i) // 2)
#     stars = "*" * i
#     print(spaces + stars)

import math

number = int(input())
if number % 2 == 0:
    number += 1

middle = math.ceil(number / 2) - 1
begin = middle
end = middle
did_we_reach_the_center = False

for i in range(number):
    for j in range(number):
        if begin <= j <= end:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    if begin == 0 and end == number - 1:
        did_we_reach_the_center = True
    if did_we_reach_the_center:
        begin += 1
        end -= 1
    else:
        begin -= 1
        end += 1

