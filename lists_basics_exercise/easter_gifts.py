gifts = input().split()
command = input()

while command != 'No Money':
    if 'OutOfStock' in command:
        type_of_command, type_of_gift = command.split()
        for i in range(len(gifts)):
            if gifts[i] == type_of_gift:
                gifts[i] = None
    elif 'Required' in command:
        type_of_command, type_of_gift, index = command.split()
        index = int(index)
        if 0 <= index < len(gifts):
            gifts[index] = type_of_gift
    elif 'JustInCase' in command:
        type_of_command, type_of_gift = command.split()
        gifts[-1] = type_of_gift

    command = input()

gifts = [gift for gift in gifts if gift is not None]

print(' '.join(gifts))