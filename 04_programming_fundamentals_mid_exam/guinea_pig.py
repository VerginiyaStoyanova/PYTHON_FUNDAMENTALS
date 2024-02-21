food_quantity_kilo = float(input())
hay_quantity_kilo = float(input())
cover_quantity_kilo = float(input())
guinea_pig_weight_kilo = float(input())

food_quantity_grams = food_quantity_kilo * 1000
hay_quantity_grams = hay_quantity_kilo * 1000
cover_quantity_grams = cover_quantity_kilo * 1000
guinea_pig_weight_grams = guinea_pig_weight_kilo * 1000
food_not_enough = False

for day in range(1, 30 + 1):
    if day % 2 == 0:
        if food_quantity_grams >= 300:
            food_quantity_grams -= 300
            need_hay = 0.05 * food_quantity_grams
            if hay_quantity_grams - need_hay >= 0 and need_hay > 0:
                hay_quantity_grams -= need_hay
            else:
                food_not_enough = True
                break
        else:
            food_not_enough = True
            break
    else:
        if food_quantity_grams >= 300:
            food_quantity_grams -= 300
    if day % 3 == 0:
        need_cover = (1 / 3) * guinea_pig_weight_grams
        if cover_quantity_grams - need_cover >= 0:
            cover_quantity_grams -= need_cover
        else:
            food_not_enough = True
            break

if food_not_enough:
    print("Merry must go to the pet store!")
else:
    food_quantity = food_quantity_grams / 1000
    hay_quantity = hay_quantity_grams / 1000
    cover_quantity = cover_quantity_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")