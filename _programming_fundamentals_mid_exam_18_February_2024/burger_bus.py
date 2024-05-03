number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    name_of_the_city = input()
    owner_income = float(input())
    owner_expenses = float(input())
    if city % 5 == 0:
        owner_income -= 0.10 * owner_income
    elif city % 3 == 0:
        owner_expenses += 0.5 * owner_expenses
    profit = owner_income - owner_expenses
    total_profit += profit
    print(f"In {name_of_the_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")