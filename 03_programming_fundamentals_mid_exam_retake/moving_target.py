targets = list(map(int, input().split()))
command = input()

while command != "End":
    command_parts = command.split()
    manipulate_command = command_parts[0]
    if manipulate_command == "Shoot":
        index = int(command_parts[1])
        power = int(command_parts[2])
        if 0 <= index < len(targets):
            shoot = targets[index] - power
            if shoot > 0:
                targets[index] = shoot
            else:
                targets.remove(targets[index])
    elif manipulate_command == "Add":
        index = int(command_parts[1])
        value = int(command_parts[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif manipulate_command == "Strike":
        index = int(command_parts[1])
        radius = int(command_parts[2])
        list_index = []
        for i in range(index - radius, index + radius + 1, 1):
            list_index.append(i)
        if any(index < 0 or index >= len(targets) for index in list_index) or \
                len(list_index) == len(targets):
            print("Strike missed!")
        else:
            del targets[index - radius:index + radius + 1]

    command = input()

print("|".join(str(target) for target in targets))