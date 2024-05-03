country_names = input().split(", ")
capitals = input().split(", ")

country_capitals_dict = dict(zip(country_names, capitals))

for country, capital in country_capitals_dict.items():
    print(f"{country} -> {capital}")