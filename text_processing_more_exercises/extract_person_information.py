import re

number = int(input())

for _ in range(number):
    string = input()
    pattern_name = r'@(\w+)\|'
    pattern_age = r'#(\d+)\*'
    matches_name = re.findall(pattern_name, string)
    matches_age = re.findall(pattern_age, string)

    print(f"{''.join(matches_name)} is {''.join(matches_age)} years old.")