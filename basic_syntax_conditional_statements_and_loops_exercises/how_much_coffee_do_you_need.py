command = input()
list_of_events = ['coding', 'dog', 'cat', 'movie']
upper_list_of_events = [word.upper() for word in list_of_events]
number_of_coffees = 0

while command != 'END':
    if command in list_of_events:
        number_of_coffees += 1
    elif command in upper_list_of_events:
        number_of_coffees += 2
    else:
        pass

    command = input()

if number_of_coffees > 5:
    print(f'You need extra sleep')
else:
    print(number_of_coffees)

# command = input()
# number_of_coffees = 0
#
# while command != 'END':
#     if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
#         number_of_coffees += 1
#     elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
#         number_of_coffees += 2
#     else:
#         pass
#
#     command = input()
#
# if number_of_coffees > 5:
#     print(f'You need extra sleep')
# else:
#     print(number_of_coffees)