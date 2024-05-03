def valid_coordinates(ships, row, column):
    if 0 <= row < len(ships) and 0 <= column < len(ships[0]):
        return True
    return False


def battle_ships(ships, battle, destroyed):
    row, column = battle
    if valid_coordinates(ships, row, column):
        if ships[row][column] > 0:
            ships[row][column] -= 1
            if ships[row][column] == 0:
                destroyed += 1
    return ships, destroyed


def main():
    number = int(input())
    ships = [list(map(int, input().split())) for _ in range(number)]

    command = [list(map(int, num.split('-'))) for num in input().split()]
    destroyed = 0

    for index, coordinates in enumerate(command):
        battle = coordinates
        ships, destroyed = battle_ships(ships, battle, destroyed)

    print(destroyed)


if __name__ == "__main__":
    main()