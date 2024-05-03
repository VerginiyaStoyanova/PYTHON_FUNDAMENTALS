def print_info(dwarfs_list):
    for dwarf in dwarfs_list:
        print(f"({dwarf[1]}) {dwarf[0]} <-> {dwarf[2]}")


dwarfs = {}

while True:
    command = input()

    if command == 'Once upon a time':
        sorted_dwarfs = sorted(dwarfs.values(), key=lambda x: (-x[2], -sum(1 for dwarf in dwarfs.values() if dwarf[1] == x[1])))
        print_info(sorted_dwarfs)
        break

    data = command.split(' <:> ')
    dwarf_name = data[0]
    dwarf_hat_color = data[1]
    dwarf_physics = int(data[2])
    if dwarf_name in dwarfs:
        if dwarf_hat_color in dwarfs[dwarf_name]:
            dwarfs[dwarf_name][dwarf_hat_color] = max(dwarfs[dwarf_name][dwarf_hat_color], dwarf_physics)
        else:
            dwarfs[dwarf_name][dwarf_hat_color] = dwarf_physics
    else:
        dwarfs[dwarf_name] = {dwarf_hat_color: dwarf_physics}
