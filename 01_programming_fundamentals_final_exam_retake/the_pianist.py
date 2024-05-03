number_of_pieces = int(input())

pieces_list = {}

for _ in range(number_of_pieces):
    command = input().split("|")
    piece = command[0]
    composer = command[1]
    key = command[2]
    pieces_list[piece] = {'composer': composer, 'key': key}

command = input()

while command != 'Stop':
    command = command.split("|")
    action = command[0]
    if action == 'Add':
        piece = command[1]
        if piece not in pieces_list:
            composer = command[2]
            key = command[3]
            pieces_list[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == 'Remove':
        piece = command[1]
        if piece in pieces_list.keys():
            del pieces_list[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        if piece in pieces_list.keys():
            pieces_list[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, info in pieces_list.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")