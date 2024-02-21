import math

budget = float(input())
price_for_one_kg_flour = float(input())

price_for_one_pack_of_eggs = 0.75 * price_for_one_kg_flour
price_of_one_liter_milk = 1.25 * price_for_one_kg_flour
cost_of_one_loaf_of_bread = price_for_one_pack_of_eggs + price_for_one_kg_flour + (price_of_one_liter_milk / 4)
loaf_of_breads = math.floor(budget / cost_of_one_loaf_of_bread)
colored_eggs = loaf_of_breads * 3
different = budget - (loaf_of_breads * cost_of_one_loaf_of_bread)

for number in range(1, loaf_of_breads + 1):
    if number % 3 == 0:
        colored_eggs -= (number - 2)

print(f"You made {loaf_of_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {different:.2f}BGN left.")
