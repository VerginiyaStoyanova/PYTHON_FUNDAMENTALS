import re

numbers = list(map(int, input().split()))

while True:
    string = input()

    if string == 'find':
        break

    message = ''

    for index, char in enumerate(string):
        new_char = chr(ord(char) - numbers[index % len(numbers)])
        message += new_char

    pattern_type = r"&(\w+)&"
    type_ = re.search(pattern_type, message)
    pattern_coo = r"<(\w+)>"
    coordinates = re.search(pattern_coo, message)
    print(f"Found {type_.group(1)} at {coordinates.group(1)}")