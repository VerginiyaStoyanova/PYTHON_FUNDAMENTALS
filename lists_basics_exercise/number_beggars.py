money_as_string = input().split(', ')
number_of_beggars = int(input())
money_as_integers = []
# money_as_integers = [int(money) for money in input().split(', ')]

for money in money_as_string:
    money_as_integers.append(int(money))
final_sums = []
start_index = 0

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)

# money_string = [int(money) for money in input().split(', ')]
# number_of_beggars = int(input())
# beggars = [0 for _ in range(number_of_beggars)]
#
# for index, money in enumerate(money_string):
#     beggars[index % number_of_beggars] += money
#
# print(beggars)
