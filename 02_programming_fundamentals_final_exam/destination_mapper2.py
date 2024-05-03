import re

string = input()

pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
matches = re.finditer(pattern, string)

places = []
for match in matches:
    places.append(match.group(2))

travel_points = 0
for place in places:
    travel_points += len(place)

print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {travel_points}")