import re

data = input()
total_income = 0

while data != "end of shift":
    pattern = r"%([A-z][a-z]+)%([^|$%.]*?)<(\w+)>([^|$%.]*?)\|(\d+)\|([^|$%.]*?)(\d+\.?\d*)\$"
    matches = re.finditer(pattern, data)

    for match in matches:
        total_price = int(match.group(5)) * float(match.group(7))
        total_income += total_price
        print(f"{match.group(1)}: {match.group(3)} - {total_price:.2f}")

    data = input()

print(f"Total income: {total_income:.2f}")