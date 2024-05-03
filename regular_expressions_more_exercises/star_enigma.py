import re

number = int(input())
attacked_planets = []
destroyed_planets = []
count_A = 0
count_D = 0

for _ in range(number):
    string = input()
    pattern = r"[star]"
    matches = re.findall(pattern, string, re.IGNORECASE)
    count = len(matches)
    decrypted_message = ""
    for char in string:
        new_char = chr(ord(char) - count)
        decrypted_message += new_char
    pattern_actions = r"@([A-Za-z]+)([^@\-!:>]*?):(\d+)([^@\-!:>]*?)!([AD])!([^@\-!:>]*?)->(\d+)"
    matches_actions = re.finditer(pattern_actions, decrypted_message)

    for match in matches_actions:
        if match.group(5) == "A":
            count_A += 1
            attacked_planets.append(match.group(1))
        elif match.group(5) == "D":
            count_D += 1
            destroyed_planets.append(match.group(1))

print(f"Attacked planets: {count_A}")
sort_planets_a = sorted(attacked_planets)
for planet in sort_planets_a:
    print(f"-> {planet}")

print(f"Destroyed planets: {count_D}")
sort_planets_d = sorted(destroyed_planets)
for planet in sort_planets_d:
    print(f"-> {planet}")