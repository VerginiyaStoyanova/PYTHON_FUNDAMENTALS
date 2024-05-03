import re

line_data = input()

demons_book = {}

pattern_names = r"[^,\s]+"
demons_names = re.findall(pattern_names, line_data)

for demon in demons_names:
    pattern_letters = r"[^0-9\+\-\*\/\.]"
    matches_l = re.findall(pattern_letters, demon)

    demons_total_health = 0
    for letter in matches_l:
        demons_total_health += ord(letter)

    demons_base_damage = 0
    pattern_numbers = r"(\-|\+)?\d+\.?\d*|\d"
    matches_n = re.finditer(pattern_numbers, demon)
    for num in matches_n:
        demons_base_damage += float(num.group())

    for char in demon:
        if char == '*':
            demons_base_damage *= 2
        elif char == '/':
            demons_base_damage /= 2

    demons_book[demon] = {'health': demons_total_health, 'damage': demons_base_damage}

for demon, status in sorted(demons_book.items()):
    health = status['health']
    damage = status['damage']
    print(f"{demon} - {health} health, {damage:.2f} damage")