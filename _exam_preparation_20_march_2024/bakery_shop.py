foods_store = {}
count_sold_food = 0
command = input()

while command != 'Complete':
    command = command.split()
    action = command[0]
    if action == 'Receive':
        quantity = int(command[1])
        if quantity > 0:
            food = command[2]
            if food not in foods_store:
                foods_store[food] = quantity
            else:
                foods_store[food] += quantity
    elif action == 'Sell':
        quantity = int(command[1])
        food = command[2]
        if food not in foods_store:
            print(f"You do not have any {food}.")
        else:
            if quantity > foods_store[food]:
                count_sold_food += foods_store[food]
                print(f"There aren't enough {food}. You sold the last {foods_store[food]} of them.")
                del foods_store[food]
            else:
                foods_store[food] -= quantity
                count_sold_food += quantity
                print(f"You sold {quantity} {food}.")
                if foods_store[food] == 0:
                    del foods_store[food]

    command = input()

for food, quantity in foods_store.items():
    print(f"{food}: {quantity}")

print(f"All sold: {count_sold_food} goods")