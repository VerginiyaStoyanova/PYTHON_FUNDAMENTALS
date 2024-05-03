command = input()
messages = []

while command != "end":
    command = command.split()
    command_action = command[0]
    if command_action == "Chat":
        message = command[1]
        messages.append(message)
    elif command_action == "Delete":
        message = command[1]
        if message in messages:
            messages.remove(message)
    elif command_action == "Edit":
        message = command[1]
        edit_message = command[2]
        if message in messages:
            index = messages.index(message)
            messages[index] = edit_message
    elif command_action == "Pin":
        message = command[1]
        if message in messages:
            messages.remove(message)
            messages.append(message)
    elif command_action == "Spam":
        command.remove('Spam')
        # for index, word in enumerate(command):
        #     messages.append(word)
        messages.extend(command)

    command = input()

for message in messages:
    print(message)