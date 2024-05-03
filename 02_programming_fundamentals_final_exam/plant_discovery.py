number = int(input())
plants = {}

for _ in range(number):
    command = input().split('<->')
    plant = command[0]
    rarity = int(command[1])
    plants[plant] = {'rarity': rarity, 'rating': []}

command = input()

while command != 'Exhibition':
    command = command.split(': ')
    action = command[0]
    plant_info = command[1]
    if action == 'Rate':
        plant, rating = plant_info.split(' - ')
        if plant in plants:
            plants[plant]['rating'].append(int(rating))
        else:
            print('error')
    elif action == 'Update':
        plant, new_rarity = plant_info.split(' - ')
        if plant in plants:
            plants[plant]['rarity'] = int(new_rarity)
        else:
            print('error')
    elif action == 'Reset':
        plant = plant_info
        if plant in plants:
            plants[plant]['rating'] = []
        else:
            print('error')

    command = input()

print(f"Plants for the exhibition:")
for plant, plant_info in plants.items():
    ratings = plant_info['rating']
    average_rating = sum(ratings) / len(ratings) if ratings else 0
    print(f"- {plant}; Rarity: {plant_info['rarity']}; Rating: {average_rating:.2f}")