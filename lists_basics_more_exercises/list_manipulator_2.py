numbers = list(map(int, input().split()))

command = input()
while command != 'end':
    if 'exchange' in command:
        type_of_command, index = command.split()
        index = int(index)
        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print('Invalid index')
    elif 'max' in command or 'min' in command:
        type_of_command, index = command.split()
        if index == 'even':
            even_numbers = [(num, index) for index, num in enumerate(numbers) if num % 2 == 0]
            if not even_numbers:
                print("No matches")
            else:
                if 'max' in command:
                    max_even_index = 0
                    max_num = -2 ** 31
                    for even_tuple in even_numbers:
                        num, index = even_tuple
                        if num >= max_num and index >= max_even_index:
                            max_num = num
                            max_even_index = index
                    print(max_even_index)
                elif 'min' in command:
                    min_even_index = 0
                    min_num = 2 ** 31
                    for even_tuple in even_numbers:
                        num, index = even_tuple
                        if num <= min_num and index >= min_even_index:
                            min_num = num
                            min_even_index = index
                    print(min_even_index)
        elif index == 'odd':
            odd_numbers = [(num, index) for index, num in enumerate(numbers) if num % 2 != 0]
            if not odd_numbers:
                print("No matches")
            else:
                if 'max' in command:
                    max_odd_index = 0
                    max_num = -2 ** 31
                    for odd_tuple in odd_numbers:
                        num, index = odd_tuple
                        if num >= max_num and index >= max_odd_index:
                            max_num = num
                            max_odd_index = index
                    print(max_odd_index)
                elif 'min' in command:
                    min_odd_index = 0
                    min_num = 2 ** 31
                    for odd_tuple in odd_numbers:
                        num, index = odd_tuple
                        if num <= min_num and index >= min_odd_index:
                            min_num = num
                            min_odd_index = index
                    print(min_odd_index)
    elif 'first' in command or 'last' in command:
        type_of_command, count, index = command.split()
        count = int(count)
        if count > len(numbers):
            print('Invalid count')
        elif index == 'even':
            even_numbers = [num for index, num in enumerate(numbers) if num % 2 == 0]
            if not even_numbers:
                print('[]')
            elif count > len(even_numbers):
                if 'first' in command:
                    print(even_numbers)
                elif 'last' in command:
                    print(even_numbers[::-1])
            else:
                list_count = []
                if 'first' in command:
                    for i in range(count):
                        list_count.append(even_numbers[i])
                    print(list_count)
                elif 'last' in command:
                    for i in range(-1, -count - 1, -1):
                        list_count.append(even_numbers[i])
                    print(list_count[::-1])
        elif index == 'odd':
            odd_numbers = [num for index, num in enumerate(numbers) if num % 2 != 0]
            if not odd_numbers:
                print('[]')
            elif count > len(odd_numbers):
                if 'first' in command:
                    print(odd_numbers)
                elif 'last' in command:
                    print(odd_numbers[::-1])
            else:
                list_count = []
                if 'first' in command:
                    for i in range(count):
                        list_count.append(odd_numbers[i])
                    print(list_count)
                elif 'last' in command:
                    for i in range(-1, -count - 1, -1):
                        list_count.append(odd_numbers[i])
                    print(list_count[::-1])

    command = input()

print(numbers)