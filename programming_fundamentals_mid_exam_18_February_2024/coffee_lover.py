coffees = input().split()
numbers = int(input())

for number in range(numbers):
    command = input().split()
    command_action = command[0]
    if command_action == "Include":
        add_coffee = command[1]
        coffees.append(add_coffee)
    elif command_action == "Remove":
        position = command[1]
        remove_numbers = int(command[2])
        if remove_numbers <= len(coffees):
            if position == "first":
                del coffees[0:remove_numbers]
            elif position == "last":
                del coffees[-remove_numbers:]
        else:
            continue
    elif command_action == "Prefer":
        index_one = int(command[1])
        index_two = int(command[2])
        if 0 <= index_one < len(coffees) and 0 <= index_two < len(coffees):
            coffees[index_one], coffees[index_two] = coffees[index_two], coffees[index_one]
        else:
            continue
    elif command_action == "Reverse":
        coffees = coffees[::-1]

print("Coffees:")
print(" ".join(coffees))