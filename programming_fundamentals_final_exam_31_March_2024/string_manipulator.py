string = input()

command = input()

while command != 'End':
    command = command.split()
    action = command[0]
    if action == 'Translate':
        char = command[1]
        replacement = command[2]
        string = string.replace(char, replacement)
        print(string)
    elif action == 'Includes':
        substring = command[1]
        if substring in string:
            print('True')
        else:
            print('False')
    elif action == "Start":
        substring = command[1]
        result = string.startswith(substring)
        print(result)
    elif action == 'Lowercase':
        string = string.lower()
        print(string)
    elif action == 'FindIndex':
        char = command[1]
        chars_list = [(index, chars) for index, chars in enumerate(string) if chars == char]
        print(chars_list[-1][0])
    elif action == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        if 0 <= start_index < len(string) and 0 <= (start_index + count) < len(string):
            string = string[:start_index] + string[start_index + count:]
        print(string)

    command = input()