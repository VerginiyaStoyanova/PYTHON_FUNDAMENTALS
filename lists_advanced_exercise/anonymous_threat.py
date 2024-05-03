def merge(merge_list, index_start, index_end):
    merge_list = merge_list[:index_start] \
                 + [''.join(merge_list[index_start:index_end + 1])] \
                 + merge_list[index_end + 1:]
    return merge_list


def divide(divide_list, target_index, parts):
    string_to_divide = divide_list[target_index]
    partition_length = len(string_to_divide) // parts
    substrings = []
    for char in range(0, len(string_to_divide), partition_length):
        length = string_to_divide[char:char + partition_length]
        if char < partition_length * parts:
            substrings.append(length)
        else:
            substrings[-1] += length
    divide_list.pop(target_index)
    divide_list = divide_list[:target_index] \
                  + substrings \
                  + divide_list[target_index:]
    return divide_list


strings = input().split()
command = input()

while command != '3:1':
    command = command.split()
    action = command[0]
    if action == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1
        strings = merge(strings, start_index, end_index)
    elif action == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        strings = divide(strings, index, partitions)

    command = input()

print(" ".join(str(text) for text in strings))