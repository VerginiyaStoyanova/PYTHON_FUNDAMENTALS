items = input().split('|')
budget = int(input())
ticket_to_france = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.5
profit = 0
list_prices = []

for item in items:
    type_of_item, price = item.split('->')
    price = float(price)
    if type_of_item == 'Clothes':
        if price <= clothes_max_price and price <= budget:
            budget -= price
            new_price = 1.4 * price
            profit += (new_price - price)
            list_prices.append("{:.2f}".format(new_price))
    elif type_of_item == 'Shoes':
        if price <= shoes_max_price and price <= budget:
            budget -= price
            new_price = 1.4 * price
            profit += (new_price - price)
            list_prices.append("{:.2f}".format(new_price))
    elif type_of_item == 'Accessories':
        if price <= accessories_max_price and price <= budget:
            budget -= price
            new_price = 1.4 * price
            profit += (new_price - price)
            list_prices.append("{:.2f}".format(new_price))

sum_of_new_prices = sum(map(float, list_prices))
final_budget = budget + sum_of_new_prices

print(' '.join(list_prices))
print(f'Profit: {profit:.2f}')

if final_budget >= ticket_to_france:
    print("Hello, France!")
else:
    print("Not enough money.")