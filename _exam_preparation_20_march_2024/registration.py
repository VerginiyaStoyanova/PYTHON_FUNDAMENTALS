username = input()
command = input()

while command != 'Registration':
    command = command.split()
    action = command[0]
    if action == 'Letters':
        if command[1] == 'Lower':
            username = username.lower()
            print(username)
        elif command[1] == 'Upper':
            username = username.upper()
            print(username)
    elif action == 'Reverse':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            reverse_string = ''
            for index in range(start_index, end_index + 1, 1):
                reverse_string += username[index]
            reverse_string = reverse_string[::-1]
            print(reverse_string)
    elif action == 'Substring':
        substring = command[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif action == 'Replace':
        char = command[1]
        username = username.replace(char, '-')
        print(username)
    elif action == 'IsValid':
        char = command[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    command = input()