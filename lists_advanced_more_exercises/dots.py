def find_largest_count_of_dots(dots, row, column, visited):
    visited[row][column] = True
    counter = 1
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + x, column + y
        # Check if the new position is valid and has not been visited
        if 0 <= new_row < len(dots) and 0 <= new_col < len(dots[0]) and \
                not visited[new_row][new_col] and dots[new_row][new_col] == '.':
            # Recursively explore the connected area
            counter += find_largest_count_of_dots(dots, new_row, new_col, visited)

    return counter


def main():
    number = int(input())
    dots = [list(input().split()) for _ in range(number)]

    # Create a 2D array to keep track of visited cells
    visited = [[False] * len(dots[0]) for _ in range(number)]

    largest_count = 0
    # Iterate through each cell to find the largest connected area of dots
    for row in range(number):
        for column in range(len(dots[0])):
            if dots[row][column] == '.' and not visited[row][column]:
                largest_count = max(largest_count, find_largest_count_of_dots(dots, row, column, visited))

    print(largest_count)


if __name__ == "__main__":
    main()