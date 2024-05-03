first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace(first_string, '')

print(second_string)

# def replace_substr(string, substring):
#     if substring not in string:
#         return string
#     string = string.replace(substring, '')
#     return replace_substr(string, substring)
#
#
# first_string = input()
# second_string = input()
#
# print(replace_substr(second_string, first_string))