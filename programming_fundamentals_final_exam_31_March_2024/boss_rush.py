import re

number = int(input())

for _ in range(number):
    is_valid = input()
    pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"
    matches = re.findall(pattern, is_valid)

    if matches:
        for match in matches:
            print(f"{match[0]}, The {match[1]}")
            print(f">> Strength: {len(match[0])}")
            print(f">> Armor: {len(match[1])}")
    else:
        print("Access denied!")