import re

list_of_participants = input().split(', ')
places = {}

while True:
    string = input()

    if string == "end of race":
        break

    pattern_name = r"([A-Za-z]+)"
    name = ''.join(re.findall(pattern_name, string))
    if name in list_of_participants:
        pattern_run = r"\d"
        sum_run_km = sum(list(map(int, re.findall(pattern_run, string))))
        if name not in places:
            places[name] = sum_run_km
        else:
            places[name] += sum_run_km

sorted_places = dict(sorted(places.items(), key=lambda item: item[1], reverse=True))
first_three_places = list(sorted_places.keys())[:3]

print(f"1st place: {first_three_places[0]}")
print(f"2nd place: {first_three_places[1]}")
print(f"3rd place: {first_three_places[2]}")