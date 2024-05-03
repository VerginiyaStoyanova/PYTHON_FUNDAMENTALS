def print_info(dwarfs_list):
    for dwarf in dwarfs_list:
        print(f"({dwarf['hat_color']}) {dwarf['name']} <-> {dwarf['physics']}")


dwarfs = []

while True:
    command = input()

    if command == 'Once upon a time':
        sorted_dwarfs = sorted(dwarfs, key=lambda x: (-x['physics'], -sum(1 for dwarf in dwarfs if dwarf['hat_color'] == x['hat_color'])))
        print_info(sorted_dwarfs)
        break

    data = command.split(' <:> ')
    dwarf_name = data[0]
    dwarf_hat_color = data[1]
    dwarf_physics = int(data[2])

    existing_dwarf = next((dwarf for dwarf in dwarfs if dwarf['name'] == dwarf_name and dwarf['hat_color'] == dwarf_hat_color), None)
    if existing_dwarf:
        existing_dwarf['physics'] = max(existing_dwarf['physics'], dwarf_physics)
    else:
        dwarfs.append({'name': dwarf_name, 'hat_color': dwarf_hat_color, 'physics': dwarf_physics})
    print(dwarfs)