time_of_the_cars = list(map(int, input().split()))
middle = len(time_of_the_cars) // 2
left_start = time_of_the_cars[:middle]
right_start = time_of_the_cars[middle + 1:]
sum_left_start = 0
sum_right_start = 0

for index in range(len(left_start)):
    if left_start[index] == 0:
        sum_left_start *= 0.8
    sum_left_start += left_start[index]

for index in range(len(right_start) - 1, -1, -1):
    if right_start[index] == 0:
        sum_right_start *= 0.8
    sum_right_start += right_start[index]

if sum_left_start < sum_right_start:
    print(f'The winner is left with total time: {sum_left_start:.1f}')
else:
    print(f'The winner is right with total time: {sum_right_start:.1f}')