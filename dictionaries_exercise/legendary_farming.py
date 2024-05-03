def check_farm_progress(dictionary):
    if dictionary["shards"] >= 250:
        dictionary["shards"] -= 250
        print(f"Shadowmourne obtained!")
        return True
    elif dictionary["fragments"] >= 250:
        dictionary["fragments"] -= 250
        print(f"Valanyr obtained!")
        return True
    elif dictionary["motes"] >= 250:
        dictionary["motes"] -= 250
        print(f"Dragonwrath obtained!")
        return True
    else:
        return False


def print_(dictionary):
    for material, quantity in dictionary.items():
        print(f"{material}: {quantity}")


def main():
    key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
    is_item_found = False

    while True:
        if is_item_found:
            break

        data = input().split()

        for index in range(0, len(data), 2):
            quantity = int(data[index])
            material = data[index + 1].lower()
            if material in key_materials:
                key_materials[material] += quantity
            else:
                key_materials[material] = quantity
            if check_farm_progress(key_materials):
                is_item_found = True
                break

    print_(key_materials)


if __name__ == "__main__":
    main()
