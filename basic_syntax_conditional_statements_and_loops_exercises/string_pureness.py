# number = int(input())
#
# for _ in range(number):
#     string = input()
#     not_pure = False
#     for character in range(len(string)):
#         if string[character] == ',' or string[character] == '.' or string[character] == '_':
#             not_pure = True
#             break
#
#     if not_pure:
#         print(f"{string} is not pure!")
#     else:
#         print(f"{string} is pure.")

number = int(input())
list_characters = [',', '.', '_']

for _ in range(number):
    string = input()
    for char in list_characters:
        if char in string:
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
