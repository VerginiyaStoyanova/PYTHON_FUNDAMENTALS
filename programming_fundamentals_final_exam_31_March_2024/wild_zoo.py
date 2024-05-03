animals_info = {}

command = input()

while command != 'EndDay':
    command = command.split(': ')
    action = command[0]
    if action == 'Add':
        info = command[1].split('-')
        animal_name = info[0]
        needed_food_quantity = int(info[1])
        area = info[2]
        if area not in animals_info:
            animals_info[area] = [{'animal_name': animal_name, 'needed_food_quantity': needed_food_quantity}]
        else:
            found = False
            for animal_info in animals_info[area]:
                if animal_info['animal_name'] == animal_name:
                    animal_info['needed_food_quantity'] += needed_food_quantity
                    found = True
                    break
            if not found:
                animals_info[area].append({'animal_name': animal_name, 'needed_food_quantity': needed_food_quantity})
    elif action == 'Feed':
        info = command[1].split('-')
        animal_name = info[0]
        food = int(info[1])
        for area, animals in animals_info.items():
            for animal in animals:
                if animal['animal_name'] == animal_name:
                    animal['needed_food_quantity'] -= food
                    if animal['needed_food_quantity'] <= 0:
                        animals.remove(animal)
                        print(f"{animal_name} was successfully fed")

    command = input()

print("Animals:")
for area, animals in animals_info.items():
    for animal in animals:
        print(f" {animal['animal_name']} -> {animal['needed_food_quantity']}g")

print("Areas with hungry animals:")
for area, animals in animals_info.items():
    if animals:
        count = sum(1 for animal in animals)
        print(f" {area}: {count}")