def find_the_position(maze_list):
    for x, row in enumerate(maze_list):
        for y, column in enumerate(row):
            if column == 'k':
                return [x, y]


def is_border(row, column, maze_list):
    if (row == 0 or row == (len(maze_list) - 1) or
            column == 0 or column == (len(maze_list[0]) - 1)):
        return True
    else:
        return False


def find_path(row, column, maze_list, counter):
    if maze_list[row][column] == '#' or maze_list[row][column] == 'x':
        return 0, False
    maze_list[row][column] = 'x'
    max_moves = counter
    any_path = False
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + x, column + y
        if 0 <= new_row < len(maze_list) and 0 <= new_col < len(maze_list[0]):
            moves, path = find_path(new_row, new_col, maze_list, counter + 1)
            max_moves = max(max_moves, moves)
            any_path = any_path or path
    if is_border(row, column, maze_list):
        return max_moves, True
    return max_moves, any_path


def print_path(longest_way, is_there_a_path):
    if is_there_a_path:
        print(f"Kate got out in {longest_way + 1} moves")
    else:
        print("Kate cannot get out")


def main():
    number = int(input())
    maze = [list(input()) for _ in range(number)]

    kate_s_position = find_the_position(maze)
    row, column = kate_s_position
    longest_way, is_there_a_path = find_path(row, column, maze, 0)
    print_path(longest_way, is_there_a_path)


if __name__ == "__main__":
    main()