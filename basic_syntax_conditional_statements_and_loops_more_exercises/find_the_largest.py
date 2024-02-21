# number = int(input())
# number_string = str(number)
# number_list = list(number_string)
# number_list.sort(reverse=True)
#
# print(''.join(number_list))

number = int(input())
sorted_number = ''.join(sorted(str(number), reverse=True))

print(sorted_number)