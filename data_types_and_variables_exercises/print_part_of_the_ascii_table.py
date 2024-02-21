# start_index = int(input())
# final_index = int(input())
#
# for index in range(start_index, final_index + 1):
#     print(chr(index), end= ' ')

# Option 2
# start_index = int(input())
# final_index = int(input())
# final_string = ''
#
# for index in range(start_index, final_index + 1):
#     final_string += f"{chr(index)} "
# print(final_string[:-1])

# Option 3
start_index = int(input())
final_index = int(input())
final_string = ''

for index in range(start_index, final_index + 1):
    final_string += f"{chr(index)} "
print(final_string.rstrip())