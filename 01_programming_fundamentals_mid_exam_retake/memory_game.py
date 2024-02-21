def is_valid_indexes(numbers_list, indexes):
    if indexes[0] == indexes[1]:
        return False
    else:
        if 0 <= indexes[0] < len(numbers_list) and 0 <= indexes[1] < len(numbers_list):
            return True
        else:
            return False


def check_the_moves(numbers):
    moves = 0
    command = input()
    while command != "end":
        moves += 1
        command_indexes = list(map(int, command.split()))
        if is_valid_indexes(numbers, command_indexes):
            if numbers[command_indexes[0]] == numbers[command_indexes[1]]:
                element = numbers[command_indexes[0]]
                for count in range(2):
                    numbers.remove(element)
                print(f"Congrats! You have found matching elements - {element}!")
                if not numbers:
                    print(f"You have won in {moves} turns!")
                    break
            else:
                print("Try again!")
        else:
            middle = len(numbers) // 2
            numbers = numbers[:middle] + [f'-{moves}a'] + [f'-{moves}a'] + numbers[middle:]
            print("Invalid input! Adding additional elements to the board")

        command = input()

    if numbers:
        print("Sorry you lose :(")
        print(" ".join(str(number) for number in numbers))


sequence = input().split()
check_the_moves(sequence)